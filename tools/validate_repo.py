"""Lightweight repository validation for CI and local checks."""
from pathlib import Path
import csv, re, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parents[1]
required=[
 'README.md','LICENSE','.gitignore','CHANGELOG.md','CONTRIBUTING.md','PORTFOLIO_NOTES.md',
 'src/index.html','data/sample/branch_master.csv','data/sample/sales_daily.csv',
 'data/sample/monthly_budget.csv','data/sample/delivery_channel.csv',
 'docs/DATA_DICTIONARY.md','docs/KPI_DEFINITIONS.md','docs/DATA_MODEL.md','docs/ARCHITECTURE.md'
]
missing=[x for x in required if not (ROOT/x).exists()]
if missing:
 print('Missing required files:', *missing, sep='\n- '); sys.exit(1)
expected={
 'branch_master.csv':['Branch','Branch Name','City','Category','Size SQM','Opening Date','Closing Date'],
 'sales_daily.csv':['Date','Branch','Core Retail Sales','Service Channel Sales','Priority Sales','Customer Count'],
 'monthly_budget.csv':['Month','Branch','Total Budget','Core Retail Budget','Service Channel Budget'],
 'delivery_channel.csv':['Date','Branch','Delivery Channel Sales']
}
for name,cols in expected.items():
 with (ROOT/'data/sample'/name).open(encoding='utf-8') as f: head=next(csv.reader(f))
 if head!=cols:
  print(f'{name}: header mismatch\nExpected: {cols}\nActual: {head}'); sys.exit(1)
html=(ROOT/'src/index.html').read_text(encoding='utf-8')
m=re.search(r'<script>([\s\S]*)</script>',html)
if not m:
 print('No inline application script found.'); sys.exit(1)
with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8') as f:
 f.write(m.group(1)); js=f.name
try:
 result=subprocess.run(['node','--check',js],capture_output=True,text=True)
 if result.returncode:
  print(result.stderr); sys.exit(result.returncode)
except FileNotFoundError:
 print('Node not available: skipped JS syntax check.')
print('Repository validation passed.')
