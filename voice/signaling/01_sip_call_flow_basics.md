# SIP Call Flow Basics

## Overview
SIP is a signaling protocol used to register endpoints, create sessions, and tear them down.

## Common Messages
- `REGISTER` — tell the platform where the endpoint lives
- `INVITE` — start a call session
- `180 Ringing` — remote side is alerting
- `200 OK` — call accepted
- `ACK` — confirm the final response
- `BYE` — end the call

## Exercises
1. Which message starts a call?
2. What does `REGISTER` accomplish?
3. Why is SIP different from RTP?

## Answer Key
1. `INVITE` starts the call setup.
2. `REGISTER` binds an endpoint identity to its reachable location.
3. SIP controls the call; RTP carries the media.
