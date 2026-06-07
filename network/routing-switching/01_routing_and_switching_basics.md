# Routing and Switching Basics

## Overview
Switches move traffic within the same local network by forwarding frames to the right port. Routers move traffic between different IP networks by choosing the next hop.

## Key Differences
- **Switch**: local segment, MAC addresses, layer 2 behavior
- **Router**: different subnets, IP addresses, layer 3 behavior
- **Default gateway**: the router a host sends traffic to when the destination is outside the local subnet

## Why Developers Care
- A wrong VLAN or switch path can isolate a service inside a subnet.
- A wrong route can send traffic to the wrong network or nowhere at all.
- Cross-subnet traffic usually hits more policy controls than same-subnet traffic.

## Exercises
1. Explain when a packet needs a router.
2. Describe what a default gateway does.
3. Give one reason switching issues can break an app deployment.

## Answer Key
1. A router is needed when the destination is on a different subnet.
2. The default gateway is the route used when the host does not have a more specific local path.
3. A bad VLAN assignment or switch port configuration can prevent hosts from reaching each other.
