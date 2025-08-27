
import os, json, re, sys
from pathlib import Path
from urllib.parse import urlparse
import requests

ROOT = Path(__file__).resolve().parent.parent  # assume script in /utilities_pack/
DATA = ROOT / "data"
AVATARS = ROOT / "avatars"
INDEX = DATA / "consultants.json"

def is_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://")

def slugify(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+","-", s.lower()).strip("-") or "consultant"

def download_image(url: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    out_path.write_bytes(r.content)
    return out_path

def load_index():
    if not INDEX.exists():
        print(f"Missing {INDEX}")
        sys.exit(1)
    return json.loads(INDEX.read_text(encoding="utf-8"))

def save_index(index):
    INDEX.write_text(json.dumps(index, indent=2), encoding="utf-8")

def save_record(rec):
    (DATA / f"{rec['id']}.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")

def main():
    index = load_index()
    changed = False
    for rec in index.get("consultants", []):
        cid = rec.get("id") or slugify(rec.get("name",""))
        rec["id"] = cid
        avatar = (rec.get("avatar") or "").strip()
        if not avatar:
            continue
        # Determine destination file
        dest = AVATARS / f"{cid}.jpg"
        if is_url(avatar):
            if dest.exists():
                print(f"[SKIP] {cid}: avatar already exists -> {dest}")
            else:
                try:
                    print(f"[GET ] {cid}: {avatar}")
                    download_image(avatar, dest)
                    print(f"[OK  ] saved -> {dest}")
                    avatar = f"./avatars/{dest.name}"
                    rec["avatar"] = avatar
                    changed = True
                except Exception as e:
                    print(f"[FAIL] {cid}: {e}")
        else:
            # local path already
            if not (ROOT / avatar.replace("./","")).exists():
                print(f"[WARN] {cid}: local avatar path not found -> {avatar}")
        # sync per-consultant file
        save_record(rec)
    if changed:
        save_index(index)
        print("Updated consultants.json")
    print("Done.")

if __name__ == "__main__":
    main()
