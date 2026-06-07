# RTP and Media Quality

## Overview
RTP carries voice media packets. Quality depends on packet timing, codec behavior, jitter buffering, and loss handling.

## Important Terms
- **Latency** — one-way delay
- **Jitter** — variation in arrival time
- **Packet loss** — dropped media packets
- **Codec** — how voice is encoded and compressed

## Exercises
1. Explain why jitter buffers exist.
2. Name one symptom of packet loss on a call.
3. Why can a network that works for file transfers still sound bad for voice?

## Answer Key
1. Jitter buffers smooth uneven packet arrival times.
2. Audio clipping, gaps, or robotic sound are common symptoms.
3. File transfers tolerate delay better than real-time audio.
