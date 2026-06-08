# Subnetting for Programmers

## Overview
Subnetting divides a larger IP range into smaller, predictable blocks. If you already understand bit masks, array slicing, or partition keys, subnetting is the same idea applied to addresses.

## Programmer-Friendly View
- An IPv4 address is a 32-bit number.
- A CIDR suffix like `/24` means the first 24 bits identify the network.
- The remaining bits identify hosts inside that network.
- More network bits means smaller subnets and fewer hosts.

## Quick Examples
- `10.0.0.0/24` -> 256 addresses, 254 usable hosts
- `10.0.0.0/26` -> 64 addresses, 62 usable hosts
- `10.0.0.64/26` -> next block after `10.0.0.0/26`

## How To Think About It
A `/24` is like reserving the first 24 bits as the partition key. A `/26` splits that same range into four smaller buckets.

## Exercises
1. Compare the host capacity of `/24` and `/26`.
2. Explain why a `/26` is useful for isolating environments.
3. Map `10.0.0.64/26` to its first and last usable host addresses.

## Answer Key
1. `/24` allows 254 usable hosts, while `/26` allows 62 usable hosts.
2. Smaller subnets reduce blast radius and make address allocation more predictable.
3. The usable range is `10.0.0.65` through `10.0.0.126`.
