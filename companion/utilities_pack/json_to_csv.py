import os, json, csv
from pathlib import Path

# ---- CONFIG: set your live base URL here (GitHub Pages root) ----
BASE_URL = "https://fgrill001.github.io/C21-contact/companion/?id={id}&v=3"
# ---------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]  # repo root
DATA = ROOT / "companion" / "data"
SEED = ROOT / "companion" / "seed"
SEED.mkdir(parents=True, exist_ok=True)

INDEX = DATA / "consultants.json"
CSV = SEED / "consultants.csv"
URLS = ROOT / "companion" / "test-urls.txt"

# read consultants index
index = json.loads(INDEX.read_text(encoding="utf-8"))
rows = index.get("consultants", [])

# write CSV (for Supabase import)
cols = ["id","name","email","phone","card_link","avatar"]
with CSV.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for rec in rows:
        w.writerow({k: rec.get(k,"") for k in cols})

# write Test URLs text file
lines = ["Consultant Test URLs:\n"]
for rec in rows:
    cid = rec.get("id","").strip()
    if not cid:
        continue
    url = BASE_URL.format(id=cid)
    lines.append(f" - {cid}\n   {url}\n")

URLS.write_text("\n".join(lines), encoding="utf-8")

print(f"Wrote CSV -> {CSV}")
print(f"Wrote URLs -> {URLS}")
