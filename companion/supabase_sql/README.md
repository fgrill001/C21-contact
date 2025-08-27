
# Supabase Setup (Quick Start)

1) Create a Supabase project → copy your PROJECT URL and ANON KEY.
2) SQL Editor → run `schema.sql`, then `policies.sql`.
3) Table editor → import `seed/consultants.csv` (generated from utilities `json_to_csv.py`).
4) In `companion/index.html`, set:
   ```html
   <script>
   window.CONFIG = {
     SUPABASE_URL: "https://YOURPROJECT.supabase.co",
     SUPABASE_ANON: "YOUR_ANON_KEY"
   };
   </script>
   ```
5) Deploy to GitHub Pages. The app will use Supabase if keys are set; otherwise it falls back to local JSON.
