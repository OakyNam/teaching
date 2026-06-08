# DHCP for Network Automation

## Overview
DHCP assigns IP configuration dynamically. Automation engineers need to understand leases because address changes, reservations, and scope exhaustion all affect scripts and devices.

## Key Concepts
- Scope or pool of assignable addresses
- Lease time and renewal
- Reservations for known devices
- Default gateway, subnet mask, and DNS options delivered with the lease

## Why It Matters
- Devices may not keep the same IP forever.
- Inventory systems should key off stable identifiers, not only addresses.
- Misconfigured scopes can strand devices outside the right subnet.

## Exercises
1. Explain the difference between a reservation and a normal lease.
2. Why can short lease times increase churn?
3. Name one problem caused by an exhausted DHCP scope.

## Answer Key
1. A reservation gives a known device a predictable address; a normal lease can vary.
2. Short lease times create more renewals and more moving addresses.
3. New devices may fail to join the network or may fall back to self-assigned addressing.
