# Supabase Setup

1) Create a Supabase project → copy your PROJECT URL and ANON KEY.
2) SQL Editor → run `schema.sql`, then `policies.sql`.
3) Create seed CSV by running `companion/utilities_pack/json_to_csv.py` → import `companion/seed/consultants.csv` into the `consultants` table.
4) In `companion/index.html` set:
```html
<script>
window.CONFIG = {
  SUPABASE_URL: "https://YOURPROJECT.supabase.co",
  SUPABASE_ANON: "YOUR_PUBLIC_ANON_KEY"
};
</script>
```
5) Commit & push. The app uses Supabase if keys are present; otherwise it falls back to local JSON.
