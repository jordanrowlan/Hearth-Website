"""Build a personal Thanksgiving Day timeline for each customer, from their exact order.

Usage: python3 build_timelines.py orders.json output.html
(orders.json is the same format build_tracker.py uses). Print the HTML to PDF:
two timelines per letter page, one cut across the middle.
Never commit order data to the repo.
"""
import sys, json, html

# Minutes before dinner, oven at 350°F. Each step: (minutes before eating, instruction)
# From Jordan's reheating cards (Muse README section 8), adjusted so everything finishes together.
PLAN = {
 "Herb-Roasted Turkey Breast": [(55, "Turkey in: lid off, pour the pan gravy over the slices, cover tightly with foil."),
                                (25, "Uncover the turkey to re-brown."),
                                (15, "Turkey out. Rest it, loosely covered.")],
 "Baked Three-Cheese Macaroni": [(50, "Mac & cheese in: lid off, cover tightly with foil."),
                                 (30, "Stir the mac & cheese gently."),
                                 (15, "Uncover the mac & cheese to crisp the top.")],
 "Mashed Potatoes": [(45, "Mashed potatoes in: lid off, cover tightly with foil."),
                     (25, "Stir the mashed potatoes."),
                     (0, "Give the mashed potatoes one last stir.")],
 "Sage Stuffing": [(40, "Sage stuffing in: lid off, cover tightly with foil."),
                   (25, "Stir the stuffing."),
                   (15, "Uncover the stuffing for a crisp top.")],
 "Gluten-Free Sage Stuffing": [(30, "Gluten-free stuffing in: lid off, cover tightly with foil."),
                               (20, "Stir the gluten-free stuffing."),
                               (10, "Uncover the gluten-free stuffing.")],
 "Classic Sweet Potatoes": [(35, "Classic sweet potatoes in: lid off, cover with foil."),
                            (10, "Uncover the sweet potatoes to toast the marshmallows. Watch closely.")],
 "Brown Butter Sweet Potatoes (No Added Sugar)": [(35, "No-added-sugar sweet potatoes in: lid off, cover with foil."),
                                                  (10, "Uncover the no-added-sugar sweet potatoes.")],
 "Green Beans with Mushrooms and Crispy Shallots": [(30, "Green beans in: lid off, cover with foil. Keep the shallot cup out."),
                                                    (15, "Stir the green beans."),
                                                    (0, "Scatter the crispy shallots on the green beans.")],
 "Honey-Thyme Roasted Carrots": [(30, "Carrots in: lid off, cover with foil."),
                                 (15, "Stir the carrots."),
                                 (5, "Uncover the carrots to caramelize the edges.")],
 "Soft Dinner Rolls": [(10, "Rolls in, lid off, to warm while the turkey rests.")],
 "Turkey Gravy": [(10, "Gravy: pour into a saucepan and warm, whisking, to a gentle simmer.")],
 "Orange Cranberry Relish": [(0, "Set out the cranberry relish, served cold.")],
}
PIES = ["Pecan Pie", "Pumpkin Pie", "Apple Crumble Pie"]
LARGE = {"Herb-Roasted Turkey Breast", "Sage Stuffing"}   # 9x13 pans
SMALL = {"Gluten-Free Sage Stuffing", "Mashed Potatoes", "Green Beans with Mushrooms and Crispy Shallots", "Classic Sweet Potatoes",
         "Brown Butter Sweet Potatoes (No Added Sugar)", "Baked Three-Cheese Macaroni", "Honey-Thyme Roasted Carrots", "Soft Dinner Rolls"}

def oven_note(items):
    big = sum(v for k, v in items.items() if k in LARGE)
    small = sum(v for k, v in items.items() if k in SMALL)
    total = big + small
    if not total:
        return ""
    parts = []
    if big: parts.append(f"{big} large 9x13 pan{'s' if big > 1 else ''}")
    if small: parts.append(f"{small} smaller pan{'s' if small > 1 else ''}")
    msg = (f"<p class='note oven'><b>Check your oven space:</b> your order has {total} foil pan{'s' if total > 1 else ''} "
           f"({' and '.join(parts)}). On Wednesday night, slide the cold pans into your oven to make sure they fit with the door closed and room for air around them. ")
    if total > 5:
        msg += ("Most home ovens hold about 4–5 pans on two racks, so plan for two rounds: reheat the turkey and stuffing first and keep them covered "
                "with foil while the sides heat (they stay hot about 20–30 minutes), or use a second oven. Switch the racks halfway so everything heats evenly.")
    else:
        msg += "Use two racks if you need to, and switch them halfway so everything heats evenly."
    return msg + "</p>"

PREP_LEAD = 45   # take food out of the fridge this long before the first dish goes in
PREHEAT = 15     # preheat before the first dish goes in

def label(m):
    if m == 0: return "Dinnertime"
    h, mm = divmod(m, 60)
    return (f"{h} hr {mm} min" if h and mm else f"{h} hr" if h else f"{mm} min") + " before"

def timeline(order):
    items = {k: v for k, v in (order.get("items") or {}).items() if v}
    plates = order.get("plates") or 0
    pans = sum(v for k, v in items.items() if k in PLAN and k not in ("Turkey Gravy", "Orange Cranberry Relish"))
    full = pans >= 6 or any(v > 1 for k, v in items.items() if k in PLAN and k not in ("Turkey Gravy", "Orange Cranberry Relish", "Soft Dinner Rolls"))
    extra = 15 if full else 0
    steps = []
    for dish, plan in PLAN.items():
        if items.get(dish):
            for m, text in plan:
                # oven-start steps move earlier for a full oven; finishing steps stay put
                steps.append((m + extra if ("in:" in text and dish not in ("Soft Dinner Rolls",)) else m, text))
    if steps:
        first = max(m for m, _ in steps)
        steps.append((first + PREHEAT, "Preheat the oven to 350°F."))
        keep = [x for x, k in (("relish", "Orange Cranberry Relish"), ("pumpkin pie", "Pumpkin Pie")) if items.get(k)]
        steps.append((first + PREHEAT + PREP_LEAD - 15, "Take your dishes out of the fridge to take the chill off." + (f" Leave the {' and '.join(keep)} chilled." if keep else "")))
        steps.append((0, "Check everything reaches 165°F in the center, then gather and enjoy."))
    grouped = {}
    for m, t in steps:
        grouped.setdefault(m, []).append(t)
    rows = sorted(grouped.items(), key=lambda kv: -kv[0])
    pies = [p for p in PIES if items.get(p)]
    return rows, pies, plates, full

def first_name(n):
    n = (n or "").strip()
    return n.split()[0].capitalize() if n and not n[0].isdigit() else "friend"

def render(orders):
    blocks = []
    for od in orders:
        rows, pies, plates, full = timeline(od)
        trs = "".join(f"<tr><td class='when'>{html.escape(label(m))}</td><td class='clock'></td><td>{'<br>'.join(html.escape(t) for t in ts)}</td></tr>" for m, ts in rows)
        extra = []
        if plates:
            extra.append(f"<p class='note'><b>Plate for One{' ×'+str(plates) if plates>1 else ''}:</b> microwave only. Lid off, pour the gravy over the turkey, cover loosely. Microwave 2–3 min in short bursts, stirring the sides. Stand 1 min, check 165°F. Start it about 5 minutes before you eat.</p>")
        if pies:
            extra.append(f"<p class='note'><b>Pie{'s' if len(pies)>1 else ''} ({', '.join(p.replace(' Pie','').replace('Apple Crumble','apple crumble').lower() for p in pies)}):</b> when you sit down to eat, take {'them' if len(pies)>1 else 'it'} out of the box and warm in the tin at 350°F for 15–25 min. {' Pumpkin is lovely chilled, too.' if 'Pumpkin Pie' in pies else ''}</p>")
        on = oven_note({k: v for k, v in (od.get("items") or {}).items() if v})
        if on:
            extra.insert(0, on)
        if full:
            extra.append("<p class='note'>Your oven will be full, so I've started the dishes 15 minutes earlier. Check the centers before serving.</p>")
        table = f"<table><thead><tr><th>Before dinner</th><th>Your time</th><th>What to do</th></tr></thead><tbody>{trs}</tbody></table>" if rows else ""
        size = "full" if len(rows) + 2 * len(extra) > 11 else "half"
        blocks.append((size, f"""<section class="tl {size}">
<div class="head"><div><div class="lab">Your Thanksgiving Day timeline</div><h1>Hi {html.escape(first_name(od.get('name')))}, here's your plan.</h1></div>
<div class="din">My dinner time:<span></span></div></div>
<p class="intro">Built just for your order, so everything comes out hot at the same time. Write your dinner time above, then fill in the clock times as you go.</p>
{table}{''.join(extra)}
<div class="foot"><span>Order {html.escape(str(od.get('order_no','')))} · Keep at or below 40°F · use within 72 hours · always check 165°F in the center</span><span class="sig">With love, Jordan</span></div>
</section>"""))
    # pair half-page timelines two to a sheet; long ones get their own sheet
    pages, pending = [], []
    for size, b in blocks:
        if size == "full": pages.append([b])
        else:
            pending.append(b)
            if len(pending) == 2: pages.append(pending); pending = []
    if pending: pages.append(pending)
    body = "".join("<div class='sheet'>" + (b[0] if len(b) == 1 else b[0].replace('class="tl half"', 'class="tl half top"', 1) + b[1]) + "</div>" for b in pages)
    css = """@page{size:8.5in 11in;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Figtree,Arial,sans-serif;color:#3A2E24}
.sheet{width:8.5in;height:11in;page-break-after:always;overflow:hidden}
.tl{width:8.5in;padding:.35in .45in;display:flex;flex-direction:column;gap:6px}
.tl.half{height:5.5in}.tl.full{height:11in}.tl.top{border-bottom:.4pt dashed #8a8a8a}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:12px}
.lab{font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;font-weight:600}
h1{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:18pt;margin:2px 0 0}
.din{font-size:10pt;font-weight:600;white-space:nowrap}.din span{display:inline-block;width:1.2in;border-bottom:.6pt solid #3A2E24;margin-left:6px}
.intro{margin:0;font-size:9pt}
table{width:100%;border-collapse:collapse;font-size:9pt}th{text-align:left;font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;border-bottom:.6pt solid #3A2E24;padding:2px 4px}
td{padding:3px 4px;border-bottom:.3pt solid #c9bfb1;vertical-align:top}td.when{white-space:nowrap;font-weight:600;width:1.15in}td.clock{width:.8in}
.note{margin:0;font-size:8.6pt}.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:.4pt solid #9a8f80;padding-top:4px;font-size:6.8pt}
.sig{font-family:'Pinyon Script',cursive;font-size:14pt;color:#914117}"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Figtree:wght@400;600&family=Pinyon+Script&display=swap"><style>{css}</style></head><body>{body}</body></html>"""

if __name__ == "__main__":
    orders = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(render(orders))
    print("timelines:", len(orders))
