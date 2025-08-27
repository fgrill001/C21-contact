
# C21 Companion Utilities

This folder contains two helper scripts:

1) `photo_downloader.py`
   - Reads `data/consultants.json`
   - For each consultant with an `avatar` URL (http/https), downloads the image into `avatars/<id>.jpg`
   - Updates `data/<id>.json` and `data/consultants.json` so `avatar` points to the local file path
   - Skips if the avatar already exists locally
   - Usage:
     ```bash
     python3 photo_downloader.py
     ```

2) `json_to_csv.py`
   - Converts `data/consultants.json` to `seed/consultants.csv` for easy import into Supabase (or Airtable).
   - Usage:
     ```bash
     python3 json_to_csv.py
     ```

## Expected repo structure

```
/companion/
  index.html
  sw.js
  manifest.webmanifest
  /data/
    consultants.json
    <id>.json ...
  /avatars/               # downloader will save images here
  /seed/                  # json_to_csv writes CSV here
```

## Notes
- Run these scripts **locally** (they need internet access and write files to your repo).
- Commit/push after running to make changes live on GitHub Pages.
