# VoIP Transport and QoS

## Overview
Voice traffic shares links with other applications, so transport design and QoS policy decide whether calls stay clear under load.

## Key Topics
- DSCP marking and trust boundaries
- WAN latency and jitter budgets
- Queueing for signaling and media traffic
- Firewall and NAT effects on voice flows

## Exercises
1. Why should bulk backups not share the same priority as voice media?
2. Explain one NAT problem that can affect VoIP.
3. Name one reason SIP and RTP may need different handling.

## Answer Key
1. Bulk traffic can crowd out low-latency audio if it gets equal treatment.
2. NAT can break address/port expectations without proper traversal support.
3. SIP is signaling traffic while RTP is real-time media traffic with stricter latency sensitivity.
