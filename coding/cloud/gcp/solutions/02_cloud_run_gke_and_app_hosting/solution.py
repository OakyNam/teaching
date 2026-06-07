"""Reference solution for Cloud Run app hosting practice."""

from __future__ import annotations

import os

try:
    import requests
except ImportError:
    requests = None


def build_service_config() -> dict[str, object]:
    return {
        'name': os.getenv('CLOUD_RUN_SERVICE', 'teaching-api'),
        'image': os.getenv('CLOUD_RUN_IMAGE', 'us-docker.pkg.dev/demo/app/teaching:latest'),
        'region': os.getenv('GCP_REGION', 'us-central1'),
        'min_instances': 0,
        'max_instances': 3,
        'ingress': 'internal-and-cloud-load-balancing',
    }


def query_service(url: str) -> dict[str, object]:
    if requests is None:
        return {'url': url, 'status': 'requests-not-installed'}

    try:
        response = requests.get(url, timeout=5)
        return {'url': url, 'status_code': response.status_code, 'ok': response.ok}
    except Exception as exc:
        return {'url': url, 'status': f'request-failed: {exc}'}


def main() -> None:
    print(build_service_config())


if __name__ == '__main__':
    main()
