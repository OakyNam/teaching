from __future__ import annotations

import os
from urllib.parse import urlencode


def build_authorization_url() -> str:
    """Build an OAuth authorization URL using environment-driven config."""
    raise NotImplementedError


def token_request_payload() -> dict[str, str]:
    """Return the payload for exchanging an authorization code for tokens."""
    raise NotImplementedError
