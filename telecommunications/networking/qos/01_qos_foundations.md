# QoS Foundations

## Overview
Quality of Service (QoS) is how networks prioritize, shape, or police traffic when bandwidth is limited. It matters when you care more about one class of traffic than another.

## Common QoS Ideas
- **Classification**: identify traffic classes such as voice, video, API, or backups
- **Marking**: attach a priority value such as DSCP
- **Queuing**: give higher-priority traffic faster access to the link
- **Shaping**: smooth traffic to a target rate
- **Policing**: drop or remark traffic that exceeds policy

## Why Application Teams Should Care
- Latency-sensitive traffic can degrade when bulk transfers fill the same path.
- A low-priority sync job should not starve user-facing API traffic.
- QoS does not create bandwidth; it decides who gets served first when contention happens.

## Exercises
1. Explain the difference between shaping and policing.
2. Name one case where API traffic deserves a higher queue.
3. Explain why QoS still needs application-level timeouts.

## Answer Key
1. Shaping delays traffic to smooth the rate; policing enforces a limit by dropping or remarking excess traffic.
2. User-facing request traffic often deserves a higher queue than batch replication or backups.
3. QoS cannot fix every outage or guarantee delivery, so the application still needs defensive timeouts and retries.
