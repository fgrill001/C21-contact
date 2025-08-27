-- Consultants table
create table if not exists public.consultants (
  id text primary key,
  name text not null,
  email text not null,
  phone text,
  card_link text,
  avatar text,
  updated_at timestamp with time zone default now()
);
alter table public.consultants enable row level security;
