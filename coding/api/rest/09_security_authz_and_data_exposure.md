# Security, Authorization, and Data Exposure

## Overview
Secure APIs do more than reject anonymous requests. They protect secrets, separate authentication from authorization, and shape responses so callers only see what they are allowed to see.

## Key Points
- Store secrets outside source files and load them from `.env` in development or a secret manager in production.
- Treat authentication as identity proofing and authorization as permission checks.
- Return the minimum response shape needed for the caller's role.
- Prefer short-lived access tokens, scoped permissions, and auditable decisions.

## Common Risks
- Hardcoded secrets or base URLs committed to the repository.
- Returning sensitive fields such as SSNs, salary, internal flags, or tokens by default.
- Trusting client-supplied roles instead of server-side permission lookup.
- Reusing broad admin tokens for automation jobs that only need one scope.

## Recommended Workflow
1. Load secrets from environment variables.
2. Validate and decode the caller identity.
3. Resolve effective permissions for the resource.
4. Build a response filtered to the allowed fields.
5. Log the decision without logging the secret itself.

## Exercises
1. Explain why `401` and `403` are different.
2. Identify which fields should be masked for a read-only user.
3. Update a demo so the signing secret comes from `.env` instead of a string literal.

## Answer Key
1. `401` means authentication is missing or invalid, while `403` means the caller is authenticated but not allowed.
2. Personal or sensitive fields like SSN, salary, and internal notes should be masked unless the role truly needs them.
3. Load the secret with `os.getenv()` after reading `.env`, then keep a safe fallback for local demos only.
