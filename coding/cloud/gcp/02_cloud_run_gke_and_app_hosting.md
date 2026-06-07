# Cloud Run, GKE, and App Hosting

## Overview
GCP offers multiple ways to run apps depending on how much platform control the team needs.

## Choosing A Platform
- **Cloud Run** for containerized apps with fast deployment and less cluster management.
- **GKE** for Kubernetes-native teams that need more scheduling and platform control.
- **Compute Engine** for VM-based workloads or legacy stacks.

## Practical Guidance
- Prefer the most managed option that still meets your operational needs.
- Standardize image building, health checks, and rollout validation.
- Keep service accounts narrow and environment-specific.
