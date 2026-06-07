# Common Port Numbers

## Overview
Ports tell an operating system which service should receive a packet after it reaches a host. Developers mostly care about ports when wiring services together, debugging connectivity, or reading firewall rules.

## Common Ports
- `22` SSH
- `53` DNS
- `80` HTTP
- `123` NTP
- `1433` SQL Server
- `3306` MySQL
- `5432` PostgreSQL
- `6379` Redis
- `8000`/`8080` local development web servers
- `443` HTTPS

## Practical Guidance
- Use well-known ports only when the protocol expects them.
- Keep application config explicit: `DB_HOST`, `DB_PORT`, `REDIS_URL`.
- Check whether a port is blocked before blaming the app.

## Exercises
1. Which port would you expect PostgreSQL to use by default?
2. Why might a service work on localhost but fail across environments?
3. Name two ports that web developers see frequently.

## Answer Key
1. PostgreSQL commonly uses `5432`.
2. A firewall, security group, ACL, or wrong port mapping may block the traffic.
3. `80` and `443`, plus `8000` or `8080` during development.
