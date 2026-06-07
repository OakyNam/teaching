# Networking Overview

## Overview
Networking is how applications move data between processes, hosts, and data centers. Every API call, database query, and browser request depends on addresses, ports, routing decisions, and transport behavior.

## What Programmers Should Understand
- IP addresses identify endpoints.
- Ports identify services on those endpoints.
- Switches move frames inside a local network.
- Routers move packets between networks.
- DNS maps names to addresses.
- TLS protects data in transit.
- Latency, bandwidth, and packet loss change application behavior.

## Mental Model
Think of a request like a package delivery:
1. DNS finds the destination address.
2. The packet reaches the local switch.
3. Routers move it across networks.
4. Firewalls or ACLs allow or deny it.
5. The server accepts it on a specific port.
6. The response travels back through the same stack.

## Exercises
1. Explain the difference between an IP address and a port.
2. Describe where DNS fits before an HTTP request.
3. List two network problems that can make a healthy application look broken.

## Answer Key
1. An IP address identifies the host; a port identifies the service on that host.
2. DNS resolves the hostname before the client opens the connection.
3. Packet loss, latency, bad routes, blocked ports, and DNS failures are common causes.
