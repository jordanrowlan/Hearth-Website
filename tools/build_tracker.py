"""Build Jordan's Thanksgiving order tracker from a JSON list of orders.

Usage: python3 build_tracker.py orders.json output.xlsx

orders.json is a list of objects with these keys (pulled from Stripe checkout sessions):
  order_no, date ("YYYY-MM-DD"), name, phone, email, address, notes,
  paid ("Yes"/"No"), items {dish name: quantity}, plates (int), sides [s1, s2, s3], total (dollars)
  Website-cart orders may instead give plate_list [[s1, s2, s3], ...], one entry per plate
  (each plate can have different sides); plates and sides are then worked out from it.
Dish names must match DISHES below. Never commit order data to the repo.
"""
import sys, json, datetime, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation

DISHES = ["Herb-Roasted Turkey Breast","Sage Stuffing","Gluten-Free Sage Stuffing","Mashed Potatoes",
  "Green Beans with Mushrooms and Crispy Shallots","Classic Sweet Potatoes","Brown Butter Sweet Potatoes (No Added Sugar)",
  "Baked Three-Cheese Macaroni","Honey-Thyme Roasted Carrots","Turkey Gravy","Orange Cranberry Relish","Soft Dinner Rolls",
  "Pecan Pie","Pumpkin Pie","Apple Crumble Pie"]
SHORT = ["Turkey","Sage Stuffing","GF Stuffing","Mashed Potatoes","Green Beans","Classic Sweet Pot.","No Added Sugar Sweet Pot.",
  "Mac & Cheese","Carrots","Gravy (qt)","Cranberry Relish","Rolls (doz)","Pecan Pie","Pumpkin Pie","Apple Pie"]
SIDES = [d for d in DISHES if d not in ("Herb-Roasted Turkey Breast","Turkey Gravy","Soft Dinner Rolls","Pecan Pie","Pumpkin Pie","Apple Crumble Pie")]
PER_PAN = {"Sage Stuffing":16,"Gluten-Free Sage Stuffing":6,"Mashed Potatoes":10,"Green Beans with Mushrooms and Crispy Shallots":10,
  "Classic Sweet Potatoes":10,"Brown Butter Sweet Potatoes (No Added Sugar)":10,"Baked Three-Cheese Macaroni":10,
  "Honey-Thyme Roasted Carrots":8,"Orange Cranberry Relish":6,"Herb-Roasted Turkey Breast":10,"Turkey Gravy":12,"Soft Dinner Rolls":12}
PKG = {"Herb-Roasted Turkey Breast":"9x13 pan + 8 oz gravy cup","Sage Stuffing":"9x13 pan","Gluten-Free Sage Stuffing":"8x8 pan",
  "Mashed Potatoes":"2-qt pan","Green Beans with Mushrooms and Crispy Shallots":"2-qt pan + shallot cup","Classic Sweet Potatoes":"2-qt pan",
  "Brown Butter Sweet Potatoes (No Added Sugar)":"2-qt pan","Baked Three-Cheese Macaroni":"2-qt pan","Honey-Thyme Roasted Carrots":"1.5-qt pan",
  "Turkey Gravy":"1-qt deli container","Orange Cranberry Relish":"1-pint deli container","Soft Dinner Rolls":"9x9 pan or bag",
  "Pecan Pie":"pie tin + box","Pumpkin Pie":"pie tin + box","Apple Crumble Pie":"pie tin + box"}

def build(orders, out, updated_note):
    F='Arial'; TERRA='914117'; OLIVE='4F5223'; YEL=PatternFill('solid',fgColor='FFF2CC')
    H=PatternFill('solid',fgColor=OLIVE); thin=Side(style='thin',color='D6C7B5')
    def font(**k): return Font(name=F,size=k.pop('size',10),**k)
    wb=openpyxl.Workbook()
    hw=wb.active; hw.title="How to use"
    lines=[("Hearth Kitchen Co. — Thanksgiving Order & Prep Tracker",dict(size=14,bold=True,color=TERRA)),
      (updated_note,dict(bold=True)),("",{}),
      ("This file is rebuilt from Stripe every evening, so you never type orders in. Edits you make here are not kept in the next rebuild,",{}),
      ("except: number your delivery stops by telling Claude the order, or fill the Stop # column on your own copy on delivery day.",{}),
      ("Prep List totals how many pans of each dish to cook (Plate for One portions are turned into pans). Delivery lists every stop.",{}),
      ("",{}),("Plate portions per pan: stuffing 16 per 9x13, GF stuffing 6 per 8x8, 2-qt sides 10, carrots 8, cranberry 6 per pint, turkey 10 per breast, gravy 12 per quart, rolls 12 per dozen.",dict(color='595959')),
      ("Private: this file holds customer names, phones and addresses. Don't share it.",dict(color='595959'))]
    for i,(t,k) in enumerate(lines,1):
        c=hw.cell(i,1,t); c.font=font(**k) if k else font(); c.alignment=Alignment(wrap_text=True,vertical='top')
    hw.column_dimensions['A'].width=120
    o=wb.create_sheet("Orders")
    o['A1']="Orders"; o['A1'].font=font(size=14,bold=True,color=TERRA)
    o['A2']=updated_note; o['A2'].font=font(italic=True,color='595959')
    hdr=["Order #","Order date","Name","Phone","Email","Delivery address","Allergies / notes","Paid?","Stop #"]+SHORT+["Plates for One","Plate side 1","Plate side 2","Plate side 3","Order total ($)"]
    for j,h in enumerate(hdr,1):
        c=o.cell(4,j,h); c.font=font(bold=True,color='FFFFFF'); c.fill=H; c.alignment=Alignment(wrap_text=True,vertical='center',horizontal='center')
    o.row_dimensions[4].height=42
    # Orders whose plates have different sides get one extra row per extra side combination.
    rows=[]
    for od in orders:
        pl=od.get("plate_list")
        if not pl:
            rows.append(od); continue
        groups=[]
        for s in pl:
            for g in groups:
                if g[0]==list(s): g[1]+=1; break
            else: groups.append([list(s),1])
        od["plates"]=len(pl)
        rows.append(dict(od,plates=groups[0][1],sides=groups[0][0]))
        for s,n in groups[1:]:
            rows.append({"order_no":f'{od.get("order_no")} (more plates)',"paid":"","plates":n,"sides":s,"items":{}})
    FIRST=5; LAST=max(FIRST+len(rows)+49, 154)
    for r in range(FIRST,LAST+1):
        for j in range(1,len(hdr)+1): o.cell(r,j).border=Border(bottom=thin); o.cell(r,j).font=font()
        o.cell(r,9).fill=YEL; o.cell(r,2).number_format='mmm d'; o.cell(r,len(hdr)).number_format='"$"#,##0.00'
    for i,od in enumerate(rows):
        r=FIRST+i; items=od.get("items",{}); sides=(od.get("sides") or [])+[None,None,None]
        d=od.get("date"); d=datetime.date.fromisoformat(d) if d else None
        row=[od.get("order_no"),d,od.get("name"),od.get("phone"),od.get("email"),od.get("address"),od.get("notes"),od.get("paid","Yes"),None]+\
            [items.get(x,0) or 0 for x in DISHES]+[od.get("plates",0) or 0,sides[0],sides[1],sides[2],od.get("total")]
        for j,v in enumerate(row,1): o.cell(r,j,v)
    for j,w in enumerate([10,9,22,13,22,32,24,7,7]+[9]*15+[8,22,22,22,10],1): o.column_dimensions[L(j)].width=w
    o.freeze_panes='D5'
    plateC=L(25); s1,s2,s3=L(26),L(27),L(28); tot=L(29)
    p=wb.create_sheet("Prep List")
    p['A1']="Prep List — what to cook"; p['A1'].font=font(size=14,bold=True,color=TERRA)
    p['A2']=updated_note; p['A2'].font=font(italic=True,color='595959')
    ph=["Dish","Full pans ordered","Plate portions","Portions per pan","Extra pans for plates","TOTAL PANS TO COOK","Packaging per pan"]
    for j,h in enumerate(ph,1):
        c=p.cell(4,j,h); c.font=font(bold=True,color='FFFFFF'); c.fill=H; c.alignment=Alignment(wrap_text=True,horizontal='center',vertical='center')
    p.row_dimensions[4].height=32
    rng=lambda col: f"Orders!${col}${FIRST}:${col}${LAST}"
    for i,d in enumerate(DISHES):
        r=5+i
        p.cell(r,1,d).font=font(bold=True); p.cell(r,2,f"=SUM({rng(L(10+i))})")
        if d in ("Herb-Roasted Turkey Breast","Turkey Gravy","Soft Dinner Rolls"): p.cell(r,3,f"=SUM({rng(plateC)})")
        elif d in SIDES: p.cell(r,3,"+".join(f'SUMPRODUCT(({rng(s)}=A{r})*{rng(plateC)})' for s in (s1,s2,s3)).join(["=",""]))
        else: p.cell(r,3,0)
        p.cell(r,4,PER_PAN.get(d,"—"))
        p.cell(r,5,f'=IF(ISNUMBER(D{r}),C{r}/D{r},0)').number_format='0.0'
        c=p.cell(r,6,f'=B{r}+E{r}'); c.number_format='0.0'; c.font=font(bold=True,color=TERRA)
        p.cell(r,7,PKG[d]).font=font(color='595959')
        for j in range(1,8):
            cc=p.cell(r,j); cc.border=Border(bottom=thin)
            if cc.font.name!=F: cc.font=font()
    r=5+len(DISHES)+1
    for k,(lab,f,fmt) in enumerate([("Plates for One to pack",f"=SUM({rng(plateC)})",None),("Orders to deliver",f'=COUNTA({rng("C")})',None),("Total sales",f"=SUM({rng(tot)})",'"$"#,##0.00')]):
        p.cell(r+k,1,lab).font=font(bold=True); c=p.cell(r+k,6,f); c.font=font(bold=True,color=TERRA)
        if fmt: c.number_format=fmt
    p.cell(r,7,"3-compartment container, sauce cup, label + reheating card, bag").font=font(color='595959')
    for k,w in zip("ABCDEFG",[44,12,12,11,13,14,44]): p.column_dimensions[k].width=w
    p.freeze_panes='B5'
    dl=wb.create_sheet("Delivery")
    dl['A1']="Delivery list — Wednesday, Nov 25"; dl['A1'].font=font(size=14,bold=True,color=TERRA)
    dl['A2']="In order received. Tell Claude your route order and the Stop # column will be filled in."; dl['A2'].font=font(italic=True,color='595959')
    dh=["Stop #","Name","Phone","Delivery address","Allergies / notes","Paid?","Plates for One","Delivered ✓"]
    for j,h in enumerate(dh,1):
        c=dl.cell(4,j,h); c.font=font(bold=True,color='FFFFFF'); c.fill=H; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
    for i,od in enumerate(orders):
        r=5+i
        for j,v in enumerate([od.get("stop"),od.get("name"),od.get("phone"),od.get("address"),od.get("notes"),od.get("paid","Yes"),od.get("plates",0) or 0],1):
            c=dl.cell(r,j,v); c.font=font(); c.border=Border(bottom=thin)
        dl.cell(r,8).fill=YEL; dl.cell(r,8).border=Border(bottom=thin)
    for k,w in zip("ABCDEFGH",[7,24,14,38,28,7,8,11]): dl.column_dimensions[k].width=w
    dl.freeze_panes='A5'
    wb.active=0; wb.save(out)

if __name__=="__main__":
    orders=json.load(open(sys.argv[1]))
    note=sys.argv[3] if len(sys.argv)>3 else f"Rebuilt from Stripe on {datetime.date.today():%b %d, %Y}: {len(orders)} orders."
    build(orders, sys.argv[2], note)
    print("built", len(orders), "orders")
