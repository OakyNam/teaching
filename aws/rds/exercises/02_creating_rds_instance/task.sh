#!/usr/bin/env bash
# TODO: Fill in the missing values for a private PostgreSQL RDS instance.
aws rds create-db-instance \
  --db-instance-identifier TODO_IDENTIFIER \
  --engine postgres \
  --db-instance-class TODO_INSTANCE_CLASS \
  --allocated-storage TODO_STORAGE_GB \
  --storage-type gp3 \
  --master-username TODO_USERNAME \
  --manage-master-user-password \
  --db-subnet-group-name TODO_SUBNET_GROUP \
  --vpc-security-group-ids TODO_SECURITY_GROUP \
  --no-publicly-accessible
