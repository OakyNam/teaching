# Environment Variables and Secret Management

## Overview
Configuration changes more often than code. Base URLs, tokens, client IDs, and secrets should live outside your Python files so you can change environments without editing source.

## Why Use `.env` In Development
- Keep local settings close to the project without committing them.
- Let one codebase run against local, staging, or production systems.
- Make secrets easy to rotate.
- Avoid copy/pasting credentials into examples.

## Recommended Layout
- Commit `.env.example` with placeholder values.
- Ignore real `.env` files in git.
- Load `.env` during local development.
- Read settings with `os.getenv()` so real environment variables can override local defaults.

## Example `.env`
```dotenv
BOOKS_API_BASE_URL=https://api.example.com
BOOKS_API_TOKEN=replace-me
JWT_SECRET=replace-me
```

## Loading Variables In Python
A lightweight dev loader can read `.env` into `os.environ`, then your code pulls values with `os.getenv()`.

## Best Practices
- Never commit production URLs with embedded credentials.
- Prefer explicit variable names like `BOOKS_API_BASE_URL` over generic names like `URL`.
- Fail fast when a required secret is missing in production.
- Keep `.env.example` realistic enough to teach the shape of the config.
- Use a secret manager instead of `.env` for deployed systems.

## Exercises
1. Move a hardcoded token out of a request example and into `.env`.
2. Explain why `.env.example` should be committed but `.env` should not.
3. Add a fallback default that keeps a local teaching demo runnable.

## Answer Key
1. Load `.env`, call `os.getenv('BOOKS_API_TOKEN')`, and use that value in the header.
2. `.env.example` documents required variables; `.env` may contain real secrets.
3. Use a safe demo fallback such as `http://127.0.0.1:8000` for a local URL or `replace-me` for a non-production token.
