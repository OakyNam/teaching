# DNS for Automation

## Overview
DNS maps names to addresses so humans and software can target services without hardcoding raw IPs everywhere.

## Why Automators Care
- Scripts break when environments move and DNS records are stale.
- Service discovery often starts with `A`, `AAAA`, `CNAME`, `SRV`, or `TXT` records.
- Troubleshooting automation frequently starts with name resolution.

## Common Record Types
- `A` / `AAAA` — host to IPv4 or IPv6 address
- `CNAME` — alias to another hostname
- `MX` — mail delivery target
- `TXT` — arbitrary metadata, verification, SPF, and more
- `SRV` — service location records used by some voice and directory systems

## Exercises
1. Explain why scripts should prefer hostnames over hardcoded IPs.
2. Describe when an `SRV` record is more useful than an `A` record.
3. Name one DNS issue that can make an API look down when the server is healthy.

## Answer Key
1. Hostnames survive infrastructure moves better than fixed addresses.
2. `SRV` records help when a client needs both host and port for a service.
3. Stale records, missing records, or bad TTL behavior can break reachability.
