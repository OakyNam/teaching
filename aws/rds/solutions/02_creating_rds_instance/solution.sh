#!/usr/bin/env bash
aws rds create-db-instance \
  --db-instance-identifier teaching-postgres \
  --engine postgres \
  --engine-version 16.3 \
  --db-instance-class db.t4g.medium \
  --allocated-storage 100 \
  --storage-type gp3 \
  --master-username app_user \
  --manage-master-user-password \
  --db-subnet-group-name teaching-private-db \
  --vpc-security-group-ids sg-0123456789abcdef0 \
  --no-publicly-accessible \
  --backup-retention-period 7
