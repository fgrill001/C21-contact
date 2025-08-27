-- Read-only for anonymous (public) via REST
create policy "Allow read for anon"
on public.consultants
for select
to anon
using (true);
