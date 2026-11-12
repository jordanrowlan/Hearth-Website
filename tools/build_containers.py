"""Adds a Containers tab (exact counts from orders.json) and a Plate for One packing guide.
Usage: python3 containers.py orders.json shopping.xlsx"""
import sys, json, collections, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
orders = json.load(open(sys.argv[1])); path = sys.argv[2]
PACK = {  # what each ordered dish goes home in
 "Herb-Roasted Turkey Breast": ["9x13 foil pan", "9x13 foil lid", "8 oz deli cup + lid (pan gravy)"],
 "Sage Stuffing": ["9x13 foil pan", "9x13 foil lid"],
 "Gluten-Free Sage Stuffing": ["8x8 foil pan", "8x8 foil lid"],
 "Mashed Potatoes": ["2-qt foil pan", "2-qt foil lid"],
 "Green Beans with Mushrooms and Crispy Shallots": ["2-qt foil pan", "2-qt foil lid", "4 oz deli cup + lid (crispy shallots)"],
 "Classic Sweet Potatoes": ["2-qt foil pan", "2-qt foil lid"],
 "Brown Butter Sweet Potatoes (No Added Sugar)": ["2-qt foil pan", "2-qt foil lid"],
 "Baked Three-Cheese Macaroni": ["2-qt foil pan", "2-qt foil lid"],
 "Honey-Thyme Roasted Carrots": ["1.5-qt foil pan", "1.5-qt foil lid"],
 "Turkey Gravy": ["32 oz (1-qt) deli container + lid"],
 "Orange Cranberry Relish": ["16 oz (1-pint) deli container + lid"],
 "Soft Dinner Rolls": ["9x9 foil pan", "9x9 foil lid"],
 "Pecan Pie": ["9-inch foil pie tin", "Pie box"], "Pumpkin Pie": ["9-inch foil pie tin", "Pie box"], "Apple Crumble Pie": ["9-inch foil pie tin", "Pie box"],
}
PLATE = ["9x9 3-compartment bagasse hinged container (PFAS-free, microwave-safe)", "2 oz portion cup + lid (gravy)", "Small bakery bag (roll)"]
WHERE = {
 "foil": "Tulsa Restaurant Equipment & Supply (9070 E 31st St, open to the public; call 918-664-1778 to check stock), Sam's Club, or WebstaurantStore online",
 "deli": "Same as foil pans: Tulsa Restaurant Equipment & Supply, Sam's Club, WebstaurantStore",
 "pie": "Tulsa Restaurant Equipment & Supply or WebstaurantStore (pie boxes come flat in 50s or 100s)",
 "bagasse": "Online: WebstaurantStore EcoChoice 9x9x3 3-compartment, no PFAS added (50-pack), or Karat Earth 9x9 (200-pack). Check the listing says PFAS-free AND microwave-safe",
 "portion": "Tulsa Restaurant Equipment & Supply, Sam's Club or WebstaurantStore (2 oz cups with lids, sleeves of 100+)",
 "bag": "Small glassine or kraft bakery bags: WebstaurantStore, Hobby Lobby, or Amazon",
 "label": "Avery printable labels (Office Depot, Target or Amazon)",
}
def where(item):
    i = item.lower()
    return WHERE["bagasse"] if "bagasse" in i else WHERE["portion"] if "portion" in i else WHERE["bag"] if "bag" in i and "bagasse" not in i else \
           WHERE["pie"] if "pie" in i else WHERE["deli"] if "deli" in i else WHERE["foil"]
cnt = collections.Counter(); dishes = 0; plates = 0
for od in orders:
    for dish, q in (od.get("items") or {}).items():
        for it in PACK.get(dish, []): cnt[it] += q
        dishes += q
    plates += len(od.get("plate_list") or []) or (od.get("plates") or 0)
for it in PLATE: cnt[it] += plates
extra = collections.OrderedDict([("Food labels (one per pan, cup and plate)", dishes + plates),
   ("Reheating cards (one per dish and plate)", dishes + plates), ("Delivery bags (one per order)", len(orders))])
import os
wb = openpyxl.load_workbook(path) if os.path.exists(path) else openpyxl.Workbook()
if not os.path.exists(path): wb.remove(wb.active)
if "Containers" in wb.sheetnames: del wb["Containers"]
ws = wb.create_sheet("Containers", 0)
T = "914117"; thin = Side(style="thin", color="D6C7B5"); F = lambda **k: Font(name="Arial", **k)
ws["A1"] = "Containers and packaging — exact counts from paid orders"; ws["A1"].font = F(size=14, bold=True, color=T)
ws["A2"] = f"{len(orders)} orders · {dishes} dishes · {plates} Plates for One. Buy a few spares of each (spills, a last-minute order)."; ws["A2"].font = F(italic=True, color="595959")
for j, h in enumerate(["Item", "Need", "+ spares", "Where to buy"], 1):
    c = ws.cell(4, j, h); c.font = F(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=T)
r = 5
rows = sorted(cnt.items()) + list(extra.items())
for item, n in rows:
    sp = max(2, -(-n // 10))
    vals = [item, n, n + sp, where(item) if item in cnt else (WHERE["label"] if "label" in item.lower() else "Print at home (cards file) / reuse tote bags" if "card" in item.lower() else "Kraft handle bags: Sam's Club, WebstaurantStore")]
    for j, v in enumerate(vals, 1):
        c = ws.cell(r, j, v); c.font = F(size=10); c.border = Border(bottom=thin); c.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
r += 1
ws.cell(r, 1, "PLATE FOR ONE: how to pack each plate").font = F(bold=True, color=T, size=12); r += 1
guide = [
 "1. Large section: about 6 oz sliced turkey. Lay the slices over one of her sides (stuffing is classic under turkey), so turkey + 1 side share the big section.",
 "2. The two small sections: her other 2 sides, about 3/4 cup each.",
 "3. If she chose Orange Cranberry Relish: it is served COLD, so pack it in its own 2 oz cup with a lid, NOT in the container. It counts as one of her 3 sides.",
 "4. Gravy: 2 oz cup with lid, set on top of the closed container. She pours it over the turkey before microwaving.",
 "5. Roll: in its own small bakery bag (it is warmed separately for 10-15 seconds).",
 "6. Close the hinged lid, add her label (name, sides, 'Microwave only'), and the Plate for One reheating card.",
 "7. Chill fully before closing the delivery bag; keep at or below 40°F until delivery.",
]
for g in guide:
    c = ws.cell(r, 1, g); c.font = F(size=10); c.alignment = Alignment(wrap_text=True, vertical="top"); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4); ws.row_dimensions[r].height = 30; r += 1
for col, w in zip("ABCD", [52, 8, 10, 70]): ws.column_dimensions[col].width = w
ws.freeze_panes = "A5"
wb.save(path); print("containers:", dict(cnt), extra)
