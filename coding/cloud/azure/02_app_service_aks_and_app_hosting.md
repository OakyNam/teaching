# App Service, AKS, and App Hosting

## Overview
Azure gives teams several ways to run apps depending on how much infrastructure ownership they want.

## Choosing A Platform
- **App Service** for managed web apps and APIs.
- **AKS** for Kubernetes-native workloads.
- **Virtual Machines** for legacy apps or custom host control.

## Practical Guidance
- Match the hosting platform to the team's operating model.
- Standardize health probes, logging, rollout steps, and rollback plans.
- Keep secrets and certificates in managed stores instead of source repos.
