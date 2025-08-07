\# CloudWatch Log Alert Lambda



Simple AWS Lambda function that listens to CloudWatch log alerts via SNS and prints useful info for monitoring.



\## Files

\- `lambda\_function.py`: AWS Lambda code

\- `event\_sample.json`: Sample test event

\- `requirements.txt`: Package needed for AWS interaction (boto3)



\## How to Use

1\. Deploy this Lambda in AWS

2\. Subscribe it to an SNS topic triggered by a CloudWatch alarm

3\. Test with the sample JSON event or real logs



