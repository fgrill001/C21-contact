
-- Read-only for anonymous (public) via REST
create policy "Allow read for anon"
on public.consultants
for select
to anon
using (true);

-- (Optional) Authenticated write policy could be added later for an admin UI.
