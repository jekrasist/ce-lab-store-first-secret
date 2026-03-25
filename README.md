# AWS Secrets Manager & IAM Instance Profile Lab

## Project Overview
This lab demonstrates how to securely handle database credentials in AWS. Instead of hardcoding passwords in the `app.py` file, we fetch them dynamically from **AWS Secrets Manager** using an **IAM Instance Profile**.

## Key Concepts Covered
- **IAM Roles**: Assigned a role to the EC2 instance so it has "permission to ask" for secrets without needing Access Keys.
- **Boto3 SDK**: Used Python to programmatically retrieve JSON secrets.
- **Secret Rotation**: Proved that updating the secret in the AWS Console/CLI immediately updates the application without a restart.

## Proof of Success
The application successfully retrieved the secret:
- **Initial State**: `InitialPassword-v1!`
- **Post-Rotation**: `RotatedPassword-v2!`
