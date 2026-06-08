# Building API Clients and Connection Pooling

## Overview
A good API client hides repetitive request code, applies timeouts consistently, and reuses network connections instead of opening a new socket for every call.

## What A Client Class Should Own
- Base URL and default headers
- Timeouts and retry policy
- Connection pool size limits
- Serialization and response parsing
- Cleanup logic for closing open connectors

## Why Pool Connections
Opening a new TCP and TLS connection for every request wastes latency and server resources. A pool lets the client reuse a small number of warm connections.

## Pooling Guidelines
- Set a maximum pool size so bursts do not create unlimited connections.
- Return healthy connections to the pool after each request.
- Close broken connections instead of reusing them.
- Expose a `close()` method or context manager for cleanup.
- Keep timeouts short enough that stuck connections do not exhaust the pool.

## Resource Management Best Practices
- Use `with` blocks or explicit `close()` calls.
- Separate pool creation from request logic.
- Track whether a connection is reusable after an exception.
- Dispose of the whole pool during shutdown or test teardown.

## Exercises
1. Build a client class that caps connections at a small number.
2. Explain why connection pooling protects both the client and server.
3. Add a context manager so the pool always closes on exit.

## Answer Key
1. Store reusable connection objects in a queue and create new ones only until the max is reached.
2. Pooling prevents socket churn, reduces handshake overhead, and avoids exhausting file descriptors or upstream limits.
3. Implement `__enter__` and `__exit__`, then call `close()` in `__exit__`.
