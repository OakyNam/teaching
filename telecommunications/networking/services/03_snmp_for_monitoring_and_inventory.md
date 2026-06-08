# SNMP for Monitoring and Inventory

## Overview
SNMP is a simple management protocol used to read counters, interface state, and device metadata from networking gear.

## What Teams Usually Use It For
- Polling interface throughput and error counters
- Collecting device identity and inventory data
- Tracking environmental and hardware health metrics
- Feeding monitoring and alerting systems

## Practical Advice
- Prefer read-only access for routine monitoring.
- Use SNMPv3 when possible for authentication and encryption.
- Document the OIDs your tooling depends on.
- Treat polling cadence like an operational budget so you do not overload weak devices.

## Exercises
1. Explain why SNMPv3 is safer than older versions.
2. Describe one inventory field commonly retrieved over SNMP.
3. Why should polling intervals stay intentional?

## Answer Key
1. SNMPv3 supports stronger security controls than community-string approaches.
2. SysName, interface descriptions, serial numbers, and software versions are common examples.
3. Polling too aggressively can waste bandwidth and device CPU.
