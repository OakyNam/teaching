# Cloud Infrastructure Fundamentals

## Overview
Cloud infrastructure gives teams on-demand compute, networking, storage, identity, and managed platform services. The names differ by provider, but the underlying concepts stay similar.

## Core Building Blocks
- **Identity and access** — users, service accounts, roles, and least privilege
- **Networking** — virtual networks, subnets, routing, DNS, and security controls
- **Compute** — virtual machines, containers, and serverless runtimes
- **Storage and data** — object storage, managed databases, caches, and queues
- **Observability** — logs, metrics, traces, and alerting
- **Delivery** — images, artifacts, pipelines, and rollback plans

## What App Teams Should Recognize
- Every cloud app still needs networking, secrets, and lifecycle management.
- Managed services reduce undifferentiated work but do not remove design responsibility.
- Provider names change, but patterns like VPC/VNet, IAM, object storage, and managed SQL repeat everywhere.

## Exercises
1. Name three cloud building blocks every application depends on.
2. Explain why managed services still require operational thinking.
3. Compare one concept that exists in AWS, GCP, and Azure under different names.

## Answer Key
1. Networking, identity, and compute are three common examples.
2. Teams still own configuration, security, cost, scaling, and failure handling.
3. Virtual networking exists as VPC-style constructs in every major provider even if the exact product name changes.
