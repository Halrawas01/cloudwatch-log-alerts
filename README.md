# CloudWatch Log Alert Lambda

This project contains an AWS Lambda function designed to listen to CloudWatch log alerts, process them, and send structured notifications via Amazon SNS. It provides a lightweight, real-time monitoring solution suitable for DevOps and security teams.

## What It Does

The Lambda function is triggered by CloudWatch Logs, extracts useful information from incoming alerts, and delivers a readable message to an SNS topic. This enables teams to stay updated on key issues such as:

- Unauthorized access attempts  
- EC2 instance failures  
- Application-level errors and exceptions  

All without logging into the AWS console.

### Sample Code Logic

```python
import boto3
import json

def lambda_handler(event, context):
    for record in event['Records']:
        message = record['Sns']['Message']
        print("ALERT:", message)
