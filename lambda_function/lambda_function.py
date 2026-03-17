import json
import boto3

sns = boto3.client("sns")

SNS_TOPIC_ARN = "SNS"


def lambda_handler(event, context):

    s3 = boto3.client("s3")

    # Get bucket and file
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)

    metrics = json.loads(response['Body'].read())

    cpu = metrics["cpu_usage_percent"]
    memory = metrics["memory_usage_percent"]
    disk = metrics["disk_usage_percent"]

    alerts = []

    if cpu > 80:
        alerts.append(f"High CPU usage: {cpu}%")

    if memory > 85:
        alerts.append(f"High memory usage: {memory}%")

    if disk > 90:
        alerts.append(f"High disk usage: {disk}%")

    if alerts:

        message = f"""
Server: {metrics['server_name']}
Timestamp: {metrics['timestamp']}

ALERTS:
{chr(10).join(alerts)}
"""

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Server Infrastructure Alert",
            Message=message
        )

    return {
        "statusCode": 200,
        "body": "Metrics processed"
    }