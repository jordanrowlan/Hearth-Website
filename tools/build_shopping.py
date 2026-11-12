"""Thanksgiving grocery list from the order tracker's Prep List and the costing workbook's recipes.
Usage: python3 build_shopping.py tracker.xlsx costing.xlsx out.xlsx
Reads the private costing workbook (kept outside this repo) for recipe quantities; writes no costs."""
import sys, math, collections, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
tracker, costing, out = sys.argv[1:4]
pl = openpyxl.load_workbook(tracker, data_only=True)['Prep List']
pans = {}
for r in range(1, pl.max_row + 1):
    d, tot = pl.cell(r, 1).value, pl.cell(r, 6).value
    if d and isinstance(tot, (int, float)) and tot > 0: pans[d] = tot
det = openpyxl.load_workbook(costing, data_only=True)['Detail']
need = collections.OrderedDict(); src = collections.defaultdict(list)
for r in range(4, det.max_row + 1):
    dish, ing, qty, unit = (det.cell(r, c).value for c in range(1, 5))
    if dish in pans and ing and isinstance(qty, (int, float)) and unit:
        u = unit.strip(); u = u[:-1] if u.endswith('s') and len(u) > 3 else u
        k = (ing.strip(), u)
        need[k] = need.get(k, 0) + qty * pans[dish]; src[k].append(dish)
def nice(q):
    return int(math.ceil(q - 1e-9)) if q >= 3 else math.ceil(q * 4 - 1e-9) / 4
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Shopping List'
T = '914117'; thin = Side(style='thin', color='D6C7B5')
ws['A1'] = 'Hearth Kitchen Co. — Thanksgiving grocery list'; ws['A1'].font = Font(name='Arial', size=14, bold=True, color=T)
ws['A2'] = 'Built from paid orders so far (pans to cook from the Prep List x each recipe). Amounts are rounded up; check pantry first.'
ws['A2'].font = Font(name='Arial', italic=True, color='595959')
hdr = ['✓', 'Ingredient', 'Amount', 'Unit', 'For']
for j, h in enumerate(hdr, 1):
    c = ws.cell(4, j, h); c.font = Font(name='Arial', bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor=T)
r = 5
for (ing, unit), q in sorted(need.items(), key=lambda kv: kv[0][0].lower()):
    for j, v in enumerate(['☐', ing, nice(q), unit, ', '.join(sorted(set(src[(ing, unit)])))], 1):
        c = ws.cell(r, j, v); c.font = Font(name='Arial', size=10); c.border = Border(bottom=thin); c.alignment = Alignment(wrap_text=True, vertical='top')
    r += 1
used = sorted({d for v in src.values() for d in v})
ws.cell(r + 1, 2, 'Pans to cook (from tracker): ' + ', '.join(f'{d} {pans[d]:.2g}' for d in used)).font = Font(name='Arial', size=9, italic=True, color='595959')
for col, w in zip('ABCDE', [4, 40, 9, 10, 46]): ws.column_dimensions[col].width = w
ws.freeze_panes = 'A5'; ws.print_title_rows = '4:4'
wb.save(out); print(len(need), 'ingredients for', len(pans), 'dishes')
