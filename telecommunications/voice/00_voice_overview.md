# Voice Overview

## Overview
Voice over IP (VoIP) systems split call handling into signaling and media. Signaling sets up the call; media carries the audio.

## Core Concepts
- SIP is commonly used for call setup and teardown.
- RTP carries the media stream.
- Call quality depends on latency, jitter, packet loss, and codec choice.
- DNS, DHCP, QoS, and firewall policy all affect real-world voice systems.

## Exercises
1. Explain the difference between signaling and media.
2. Name two non-voice network services that still affect voice systems.
3. Why does packet loss matter more for voice than many batch jobs?

## Answer Key
1. Signaling manages call state; media carries the audio payload.
2. DNS and DHCP are common examples, along with NTP and QoS policy.
3. Voice traffic is real time, so missing packets are heard immediately.
