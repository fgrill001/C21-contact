import os, json, re, sys
from pathlib import Path
from urllib.parse import urlparse
import requests

# Resolve repo root robustly: try parents[2] (repo), then parents[1] (companion), fallback to CWD
HERE = Path(__file__).resolve()
CANDIDATES = [
    HERE.parents[2],   # .../C21-contact
    HERE.parents[1],   # .../companion
    Path.cwd()         # current working dir
]
ROOT = None
for c in CANDIDATES:
    if (c / "companion" / "data" / "consultants.json").exists():
        ROOT = c
        break
if ROOT is None:
    # last attempt: if we're already inside .../companion, treat that as ROOT
    if (HERE.parents[1] / "data" / "consultants.json").exists():
        ROOT = HERE.parents[1].parent  # go up to repo root
    else:
        print("Could not locate companion/data/consultants.json from:", HERE)
        sys.exit(1)

DATA = ROOT / "companion" / "data"
AVATARS = ROOT / "companion" / "avatars"
INDEX = DATA / "consultants.json"

def is_url(s: str) -> bool:
    return isinstance(s, str) and (s.startswith("http://") or s.startswith("https://"))

def slugify(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", (s or "").lower()).strip("-") or "consultant"

def download_image(url: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    out_path.write_bytes(r.content)
    return out_path

def main():
    print("Repo ROOT =", ROOT)
    print("Reading  =", INDEX)
    index = json.loads(INDEX.read_text(encoding="utf-8"))

    changed = False
    for rec in index.get("consultants", []):
        cid = rec.get("id") or slugify(rec.get("name"))
        rec["id"] = cid
        avatar = (rec.get("avatar") or "").strip()
        if not avatar:
            continue

        dest = AVATARS / f"{cid}.jpg"
        if is_url(avatar):
            if dest.exists():
                print(f"[SKIP] {cid}: already have {dest.name}")
            else:
                try:
                    print(f"[GET ] {cid}: {avatar}")
                    download_image(avatar, dest)
                    print(f"[OK  ] saved -> {dest}")
                except Exception as e:
                    print(f"[FAIL] {cid}: {e}")
                    continue
            rec["avatar"] = f"./avatars/{dest.name}"
            changed = True
        else:
            # local path — verify it exists
            local = (ROOT / "companion" / avatar.replace("./", ""))
            if not local.exists():
                print(f"[WARN] {cid}: local avatar path not found -> {avatar}")
        # sync per-consultant file
        (DATA / f"{cid}.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")

    if changed:
        INDEX.write_text(json.dumps(index, indent=2), encoding="utf-8")
        print("Updated consultants.json")
    print("Done.")

if __name__ == "__main__":
    main()
