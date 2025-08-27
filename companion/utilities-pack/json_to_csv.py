
import os, json, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SEED = ROOT / "seed"
SEED.mkdir(parents=True, exist_ok=True)

INDEX = DATA / "consultants.json"
CSV = SEED / "consultants.csv"

index = json.loads(INDEX.read_text(encoding="utf-8"))
cols = ["id","name","email","phone","card_link","avatar"]
with CSV.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for rec in index.get("consultants", []):
        row = {k: rec.get(k,"") for k in cols}
        w.writerow(row)

print(f"Wrote {CSV}")
