#!/usr/bin/env python3
"""Weekly client invoice + grocery statement, in the Hearth house style.

Usage:
    python3 tools/weekly_statement.py <data.json> <out_dir>

Writes <out_dir>/Invoice_<invoice_no>.pdf and <out_dir>/Grocery_Statement_<invoice_no>.pdf.

All client details, rates and amounts come from the JSON file, which is built
from the private Hearth Invoice Tracker. Never commit that JSON: it holds
client names and prices. This script holds only the layout.

JSON shape (money as numbers):
{
  "invoice_no": "HKC-2026-0101",
  "invoice_date": "January 1, 2026",
  "service_week": "December 26 – 31, 2025",
  "billed_to": "Client name",
  "from_lines": ["Chef name", "Business name · City, State"],
  "service": {"description": "...", "detail": "Cook days ...", "qty": "1 week", "rate": 0},
  "mileage": {"miles": 0, "rate": 0, "detail": "IRS standard business rate"},
  "client_name": "First name",               # used in "<name>'s grocery fund"
  "prepared_for": "Client full name",
  "purchases": [                             # every purchase since the last deposit
     {"date": "Jan 1", "store": "Store", "for": "Cook day",
      "subtotal": 0, "tax": 0, "discount": 0, "total": 0,
      "new": true}                           # new = not on an earlier invoice
  ],
  "fund": {"carried": 0, "new": 0, "label": "the weeks starting <date>"},
  "payment_note": "Payment by Zelle, check or cash, payable to Hearth Kitchen Co., LLC."
}
"""
import html
import json
import os
import subprocess
import sys
import tempfile

STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600&display=swap');
@page { size: letter; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Inter, Helvetica, Arial, sans-serif; color: #3A2A1E; font-size: 9.5pt; }
.page { width: 8.5in; min-height: 11in; padding: 0.5in 0.65in 0.35in; background: #F8EEDF; }
.bar { display: flex; height: 7px; border-radius: 3px; overflow: hidden; margin: -0.3in -0.32in 0.32in; }
.bar span { flex: 1; } .b1{background:#7E2F14}.b2{background:#C4581C}.b3{background:#DDA238}.b4{background:#86893B}
.eyebrow { font-size: 8.5pt; letter-spacing: .22em; text-transform: uppercase; color: #7A5A44; font-weight: 500; }
h1 { font-family: Lora, Georgia, serif; font-weight: 500; font-size: 30pt; margin: 2px 0 0; color: #3A2418; }
.serif { font-family: Lora, Georgia, serif; }
h2 { font-family: Lora, Georgia, serif; font-weight: 400; color: #A94818; letter-spacing: .12em; text-transform: uppercase; font-size: 12pt; margin: 14px 0 6px; }
.head { display: flex; justify-content: space-between; align-items: flex-start; }
.meta { text-align: right; line-height: 1.75; color: #6A5444; } .meta b { color: #3A2418; font-weight: 600; }
.cards { display: flex; gap: 14px; margin: 14px 0 6px; }
.card { flex: 1; background: #F5DDBC; border-radius: 10px; padding: 12px 16px 14px; line-height: 1.55; }
.card .lab { font-size: 8pt; letter-spacing: .16em; text-transform: uppercase; color: #A94818; font-weight: 600; margin-bottom: 6px; }
table { width: 100%; border-collapse: collapse; }
th { font-size: 8pt; letter-spacing: .14em; text-transform: uppercase; color: #A94818; font-weight: 600; text-align: left; padding: 6px 8px; border-bottom: 2px solid #C4581C; }
td { padding: 5px 8px; border-bottom: 1px solid #E7CFAE; vertical-align: top; }
.r { text-align: right; white-space: nowrap; } td:first-child { white-space: nowrap; } .sub { color: #7A6252; font-size: 9pt; }
tr.tot td { font-weight: 600; border-top: 2px solid #C4581C; border-bottom: 0; }
.due { display: flex; justify-content: space-between; align-items: center; background: #C4581C; color: #fff; border-radius: 10px; padding: 11px 22px; margin: 12px 0 2px; }
.due .lab { font-size: 9pt; letter-spacing: .22em; font-weight: 500; }
.due .amt { font-family: Lora, Georgia, serif; font-size: 24pt; }
.note { color: #6A5444; font-size: 9pt; margin: 10px 0 0; }
.sign { text-align: center; margin-top: 10px; color: #6A5444; line-height: 1.5; }
.sign .name { font-family: Lora, Georgia, serif; font-style: italic; font-size: 17pt; color: #3A2418; }
.tag { text-align: center; font-family: Lora, Georgia, serif; font-style: italic; color: #A94818; margin-top: 12px; }
.stats { display: flex; gap: 14px; margin: 16px 0 6px; }
.stat { flex: 1; background: #F5DDBC; border-radius: 10px; text-align: center; padding: 11px 8px 12px; }
.stat .lab { font-size: 8pt; letter-spacing: .16em; text-transform: uppercase; color: #A94818; font-weight: 600; }
.stat .v { font-family: Lora, Georgia, serif; font-size: 20pt; margin-top: 4px; }
.stat.hot { background: #C4581C; color: #fff; } .stat.hot .lab { color: #FBE6D3; }
.center { text-align: center; }
"""


def money(x):
    return ("−" if x < 0 else "") + "${:,.2f}".format(abs(x))


def esc(s):
    return html.escape(str(s or ""))


def bar():
    return '<div class="bar"><span class="b1"></span><span class="b2"></span><span class="b3"></span><span class="b4"></span></div>'


def sign(opening):
    return (f'<div class="sign">{opening}<div class="name">Jordan</div>Hearth Kitchen Co.</div>'
            '<div class="tag">Nourishing your body starts with how you treat your food.</div>')


def build(d):
    svc = d["service"]
    mil = d["mileage"]
    svc_amt = round(svc["rate"], 2)
    mil_amt = round(mil["miles"] * mil["rate"], 2)
    total = round(svc_amt + mil_amt, 2)
    purchases = d["purchases"]
    new = [p for p in purchases if p.get("new")]
    new_sum = round(sum(p["total"] for p in new), 2)
    fund = round(d["fund"]["carried"] + d["fund"]["new"], 2)
    spent = round(sum(p["total"] for p in purchases), 2)
    remaining = round(fund - spent, 2)
    who = esc(d["client_name"])

    from_html = "<br>".join(esc(x) for x in d["from_lines"])
    grocery_rows = "".join(
        f'<tr><td>{esc(p["date"])}</td><td>{esc(p["store"])}</td><td class="r">{money(p["total"])}</td></tr>' for p in new
    ) or '<tr><td colspan="3" class="sub">No new grocery purchases this week.</td></tr>'
    invoice = f"""<!doctype html><html><head><meta charset="utf-8"><style>{STYLE}</style></head><body><div class="page">
{bar()}
<div class="head"><div><div class="eyebrow">Hearth Kitchen Co., LLC</div><h1>Invoice</h1></div>
<div class="meta"><b>Invoice</b> {esc(d["invoice_no"])}<br><b>Invoice date</b> {esc(d["invoice_date"])}<br><b>Service week</b> {esc(d["service_week"])}<br><b>Due</b> Upon receipt</div></div>
<div class="cards"><div class="card"><div class="lab">Billed to</div>{esc(d["billed_to"])}</div>
<div class="card"><div class="lab">From</div>{from_html}</div></div>
<h2>Services</h2>
<table><tr><th>Description</th><th class="r">Qty</th><th class="r">Rate</th><th class="r">Amount</th></tr>
<tr><td>{esc(svc["description"])}<div class="sub">{esc(svc.get("detail"))}</div></td><td class="r">{esc(svc.get("qty", "1 week"))}</td><td class="r">{money(svc["rate"])}</td><td class="r">{money(svc_amt)}</td></tr>
<tr><td>Mileage<div class="sub">{esc(mil.get("detail", "IRS standard business rate"))}</div></td><td class="r">{mil["miles"]:g} mi</td><td class="r">{money(mil["rate"])}</td><td class="r">{money(mil_amt)}</td></tr>
<tr class="tot"><td colspan="3">Total due</td><td class="r">{money(total)}</td></tr></table>
<div class="due"><span class="lab">AMOUNT DUE</span><span class="amt">{money(total)}</span></div>
<h2>Groceries</h2>
<div style="margin-bottom:8px">Paid from {who}'s grocery fund at cost, with no markup. Not included in the amount due.</div>
<table><tr><th style="width:18%">Date</th><th>Store</th><th class="r">Amount</th></tr>{grocery_rows}
<tr><td colspan="2"><b>Groceries since last invoice</b></td><td class="r"><b>{money(new_sum)}</b></td></tr>
<tr><td colspan="2">Grocery fund available for {esc(d["fund"]["label"])}</td><td class="r">{money(fund)}</td></tr>
<tr class="tot"><td colspan="2">Remaining grocery fund</td><td class="r">{money(remaining)}</td></tr></table>
<p class="note">{esc(d["payment_note"])} Receipts are available on request. Thank you for trusting me with {who}'s table.</p>
{sign("With love,")}
</div></body></html>"""

    def ts(p):
        parts = []
        if p.get("tax"):
            parts.append(f'+{money(p["tax"])} tax')
        if p.get("discount"):
            parts.append(f'−{money(p["discount"])} discount')
        return "<br>".join(parts) or esc(p.get("tax_note", "tax included"))

    prow = "".join(
        f'<tr><td>{esc(p["date"])}</td><td>{esc(p["store"])}</td><td>{esc(p.get("for"))}</td>'
        f'<td class="r">{money(p["subtotal"]) if p.get("subtotal") else "—"}</td><td class="r">{ts(p)}</td><td class="r">{money(p["total"])}</td></tr>'
        for p in purchases)
    statement = f"""<!doctype html><html><head><meta charset="utf-8"><style>{STYLE}</style></head><body><div class="page">
{bar()}
<div class="center"><div class="eyebrow">Hearth Kitchen Co.</div><h1>Grocery Statement</h1>
<div class="sub" style="font-size:10.5pt;margin-top:4px">Prepared for {esc(d["prepared_for"])} · Statement date {esc(d["invoice_date"])}</div></div>
<div class="stats"><div class="stat"><div class="lab">Grocery fund</div><div class="v">{money(fund)}</div></div>
<div class="stat"><div class="lab">Spent to date</div><div class="v">{money(spent)}</div></div>
<div class="stat hot"><div class="lab">Remaining</div><div class="v">{money(remaining)}</div></div></div>
<h2>Purchases</h2>
<table><tr><th>Date</th><th>Store</th><th>For</th><th class="r">Subtotal</th><th class="r">Tax / savings</th><th class="r">Total</th></tr>{prow}
<tr class="tot"><td colspan="5">Total spent</td><td class="r">{money(spent)}</td></tr></table>
<h2>Fund balance</h2>
<table><tr><td>Carried over from last grocery fund</td><td class="r">{money(d["fund"]["carried"])}</td></tr>
<tr><td>New grocery money provided</td><td class="r">{money(d["fund"]["new"])}</td></tr>
<tr><td>Available for {esc(d["fund"]["label"])}</td><td class="r">{money(fund)}</td></tr>
<tr><td>Less purchases to date</td><td class="r">{money(-spent)}</td></tr>
<tr class="tot"><td>Remaining balance</td><td class="r">{money(remaining)}</td></tr></table>
<p class="note">Groceries are purchased for {who}'s household at cost, with no markup. Itemized receipts are available on request.</p>
{sign("Thank you,")}
</div></body></html>"""
    return invoice, statement, {"total": total, "new_groceries": new_sum, "spent": spent, "remaining": remaining}


PRINT_JS = """
const { chromium } = require('playwright');
(async () => {
  const [,, ...pairs] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage();
  for (let i = 0; i < pairs.length; i += 2) {
    await p.goto('file://' + pairs[i], { waitUntil: 'networkidle' });
    await p.pdf({ path: pairs[i + 1], format: 'Letter', printBackground: true });
  }
  await b.close();
})();
"""


def main():
    data_path, out_dir = sys.argv[1], sys.argv[2]
    d = json.load(open(data_path))
    invoice, statement, totals = build(d)
    os.makedirs(out_dir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    inv_html, st_html = os.path.join(tmp, "invoice.html"), os.path.join(tmp, "statement.html")
    open(inv_html, "w").write(invoice)
    open(st_html, "w").write(statement)
    inv_pdf = os.path.join(out_dir, f'Invoice_{d["invoice_no"]}.pdf')
    st_pdf = os.path.join(out_dir, f'Grocery_Statement_{d["invoice_no"]}.pdf')
    js = os.path.join(tmp, "print.js")
    open(js, "w").write(PRINT_JS)
    subprocess.run(["node", js, inv_html, inv_pdf, st_html, st_pdf], check=True, cwd="/tmp")
    print(json.dumps({"invoice": inv_pdf, "statement": st_pdf, **totals}))


if __name__ == "__main__":
    main()
