# OAuth Setup and Token Flows

## Overview
OAuth lets an application obtain scoped access to another system without directly sharing a user's password. The client receives tokens with limited scope and lifetime.

## Common Roles
- **Resource owner** — the user or service whose data is being accessed
- **Client** — the application asking for access
- **Authorization server** — the identity provider issuing tokens
- **Resource server** — the API that validates tokens

## Common Flows
- **Authorization code + PKCE** — best for browser and mobile apps
- **Client credentials** — best for service-to-service calls
- **Refresh token** — get a new access token without repeating the full login flow

## Setup Checklist
1. Register the application with the identity provider.
2. Capture the client ID and, when appropriate, the client secret.
3. Configure the redirect URI.
4. Request the minimum scopes required.
5. Exchange the code for tokens at the token endpoint.
6. Store tokens securely and refresh them before expiry.

## Best Practices
- Use PKCE for public clients.
- Never commit client secrets.
- Keep scopes narrow and environment-specific.
- Validate issuer, audience, expiry, and signature on the API side.
- Log token metadata, not token values.

## Exercises
1. Decide whether a browser app should use PKCE or client credentials.
2. List the minimum variables needed in `.env` for a local OAuth demo.
3. Explain why scopes should stay narrow.

## Answer Key
1. A browser app should use authorization code with PKCE.
2. Client ID, redirect URI, auth URL, token URL, and only a client secret when the client type allows it.
3. Narrow scopes reduce blast radius when a token is leaked or misused.
