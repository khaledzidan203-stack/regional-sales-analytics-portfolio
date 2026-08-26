"""Generate deterministic synthetic data for the public portfolio repository."""
from __future__ import annotations
import csv, math, random
from calendar import monthrange
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "sample"
OUT.mkdir(parents=True, exist_ok=True)
random.seed(42)

BRANCHES = [
    ("B001", "North Hub", "Metro North", "Flagship", 240, date(2024, 1, 1), None),
    ("B002", "North Point", "Metro North", "Standard", 160, date(2024, 1, 1), None),
    ("B003", "North Square", "Metro North", "Standard", 125, date(2024, 3, 1), None),
    ("B004", "Central Hub", "Metro Central", "Flagship", 220, date(2024, 1, 1), None),
    ("B005", "Central Point", "Metro Central", "Standard", 150, date(2024, 1, 1), None),
    ("B006", "Central Mini", "Metro Central", "Compact", 80, date(2024, 1, 1), date(2026, 5, 31)),
    ("B007", "East Point", "Metro East", "Standard", 135, date(2025, 10, 1), None),
    ("B008", "East Mini", "Metro East", "Compact", 75, date(2024, 1, 1), None),
]
BASE = {"B001":7200,"B002":5000,"B003":4300,"B004":6800,"B005":4700,"B006":3300,"B007":3900,"B008":3000}
SERVICE_MIX = {"B001":.28,"B002":.20,"B003":.16,"B004":.30,"B005":.18,"B006":.15,"B007":.12,"B008":.14}
DELIVERY_PCT = {"B001":.045,"B002":.035,"B004":.050,"B005":.030,"B007":.040}

with (OUT / "branch_master.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Branch","Branch Name","City","Category","Size SQM","Opening Date","Closing Date"])
    for b in BRANCHES:
        w.writerow([b[0],b[1],b[2],b[3],b[4],b[5].isoformat(),b[6].isoformat() if b[6] else ""])

sales, delivery = [], []
d = date(2025, 1, 1)
while d <= date(2026, 8, 15):
    season = 1 + 0.06 * math.sin((d.timetuple().tm_yday / 365) * 2 * math.pi)
    weekend = 0.88 if d.weekday() == 4 else (1.04 if d.weekday() in (3, 5) else 1.0)
    for code, _, _, _, _, opened, closed in BRANCHES:
        if d < opened or (closed and d > closed):
            continue
        year_factor = 1.0
        if d.year == 2026:
            year_factor = 0.88 if d < date(2026, 5, 15) else 0.98
            if code in ("B001", "B004"): year_factor += 0.04
            if code in ("B003", "B008"): year_factor -= 0.05
        ramp = min(1.0, 0.55 + (d - opened).days / 220) if code == "B007" else 1.0
        total = BASE[code] * season * weekend * year_factor * ramp * random.uniform(0.90, 1.10)
        service = total * SERVICE_MIX[code] * random.uniform(.92, 1.08)
        core = max(0, total - service)
        priority = core * random.uniform(.36, .49)
        customers = max(1, round(total / random.uniform(66, 82)))
        sales.append([d.isoformat(), code, round(core,2), round(service,2), round(priority,2), customers])
        if d >= date(2026, 1, 1) and code in DELIVERY_PCT:
            amount = core * DELIVERY_PCT[code] * random.uniform(.85, 1.15)
            delivery.append([d.isoformat(), code, round(amount,2)])
    d += timedelta(days=1)

# Intentional review cases so the Data Quality page is demonstrable.
sales.append(sales[100].copy())
review_row = sales[250].copy(); review_row[5] = 0; sales.append(review_row)

with (OUT / "sales_daily.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["Date","Branch","Core Retail Sales","Service Channel Sales","Priority Sales","Customer Count"]); w.writerows(sales)
with (OUT / "delivery_channel.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["Date","Branch","Delivery Channel Sales"]); w.writerows(delivery)
with (OUT / "monthly_budget.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["Month","Branch","Total Budget","Core Retail Budget","Service Channel Budget"])
    for month in range(1, 13):
        for code, _, _, _, _, opened, closed in BRANCHES:
            month_start = date(2026, month, 1)
            if month_start < date(opened.year, opened.month, 1) or (closed and month_start > date(closed.year, closed.month, 1)):
                continue
            total_budget = BASE[code] * monthrange(2026, month)[1] * 1.01
            service_budget = total_budget * SERVICE_MIX[code]
            w.writerow([f"2026-{month:02d}", code, round(total_budget,2), round(total_budget-service_budget,2), round(service_budget,2)])

print(f"Generated {len(sales):,} sales rows and {len(delivery):,} delivery rows.")
