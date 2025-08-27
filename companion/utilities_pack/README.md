# C21 Companion Utilities

## photo_downloader.py
- Reads `companion/data/consultants.json`
- Downloads any HTTP(S) avatar URLs to `companion/avatars/<id>.jpg`
- Rewrites JSON to use local `./avatars/<id>.jpg`
- Skips files that already exist

Usage:
```bash
# from repo root, with Python + requests installed
python companion/utilities_pack/photo_downloader.py
```

## json_to_csv.py
- Converts `companion/data/consultants.json` to `companion/seed/consultants.csv` for Supabase import.

Usage:
```bash
python companion/utilities_pack/json_to_csv.py
```

After running either utility: commit & push to update GitHub Pages.
