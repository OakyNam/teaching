# REST Best Practices Index

Use this file as the jump page instead of trying to memorize every practice at once.

## Learn In This Order
1. [REST Fundamentals](./00_rest_fundamentals.md) — understand resources, HTTP verbs, status codes, and how to interact with endpoints.
2. [API Design Principles](./01_api_design_principles.md) — model resources and stable URL patterns.
3. [Environment Variables and Secret Management](./11_environment_variables_and_secret_management.md) — keep URLs and credentials out of source files.
4. [Building API Clients and Connection Pooling](./12_building_api_clients_and_connection_pooling.md) — build reusable client classes without over-creating connections.
5. [Security, Authorization, and Data Exposure](./09_security_authz_and_data_exposure.md) — protect secrets and shape responses safely.
6. [OAuth Setup and Token Flows](./13_oauth_setup_and_token_flows.md) — integrate with identity providers correctly.

## Operational Themes
- Design endpoints that are predictable and observable.
- Keep configuration in `.env` for local development and secret managers in deployed systems.
- Reuse connections, enforce timeouts, and close connectors cleanly.
- Prefer small, focused lessons over one giant best-practices document.
