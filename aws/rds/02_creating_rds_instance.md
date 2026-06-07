# 02 - Creating an RDS Instance

## Overview
Provisioning an RDS instance is mostly about choosing safe defaults: a private deployment, the right engine version, durable backups, and a network path that only your application can reach.

## Console Walkthrough
1. Open **RDS → Databases → Create database**.
2. Choose **PostgreSQL** (or MySQL if required).
3. Pick a production-ready template, or start with dev/test for experiments.
4. Set the **DB instance identifier**, admin username, and store the password in **AWS Secrets Manager**.
5. Choose an **instance class** and **storage type** (`gp3` is a strong default).
6. Attach the correct **VPC**, **DB subnet group**, and **security group**.
7. Disable **public access** unless there is a very specific operational reason.
8. Enable automated backups, choose a maintenance window, and create the instance.

## AWS CLI Equivalents
```bash
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
  --backup-retention-period 7 \
  --multi-az

aws rds describe-db-instances --db-instance-identifier teaching-postgres
```

## Terraform Example
```hcl
resource "aws_db_subnet_group" "teaching" {
  name       = "teaching-private-db"
  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]
}

resource "aws_db_instance" "teaching" {
  identifier                  = "teaching-postgres"
  engine                      = "postgres"
  engine_version              = "16.3"
  instance_class              = "db.t4g.medium"
  allocated_storage           = 100
  storage_type                = "gp3"
  db_name                     = "teaching"
  username                    = "app_user"
  manage_master_user_password = true
  db_subnet_group_name        = aws_db_subnet_group.teaching.name
  vpc_security_group_ids      = [aws_security_group.db.id]
  publicly_accessible         = false
  backup_retention_period     = 7
  multi_az                    = true
  skip_final_snapshot         = false
}
```

## Key Parameters to Understand
- **engine / engine_version** — match your framework and extension requirements.
- **instance class** — determines compute and memory headroom.
- **storage** — size plus type (`gp3`, `io1`, `io2`).
- **credentials** — prefer managed secrets over plaintext passwords.
- **VPC config** — subnets, route tables, and security groups decide who can reach the instance.

## Security Best Practices
- Keep the database in **private subnets**.
- Set **`publicly_accessible = false`**.
- Store credentials in **AWS Secrets Manager** and rotate when possible.
- Limit inbound security group rules to application security groups, not wide CIDR ranges.
- Turn on **storage encryption** and use TLS for client connections.

## Connection String Formats
```text
postgresql://app_user:<password>@teaching-postgres.abc123.us-east-1.rds.amazonaws.com:5432/teaching
mysql+pymysql://app_user:<password>@teaching-mysql.abc123.us-east-1.rds.amazonaws.com:3306/teaching
```

## Practice
- Exercise: [exercises/02_creating_rds_instance/task.sh](./exercises/02_creating_rds_instance/task.sh)
- Solution: [solutions/02_creating_rds_instance/solution.sh](./solutions/02_creating_rds_instance/solution.sh)

⬅️ Previous: [01 - RDS Overview](./01_rds_overview.md)
➡️ Next: [03 - Connecting and Operations](./03_connecting_and_operations.md)
