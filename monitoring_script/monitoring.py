import json
import psutil
import boto3
import socket
from datetime import datetime, UTC
from botocore.exceptions import ClientError

# =============================
# Configuration
# =============================
BUCKET_NAME = "Your_BUCKET_NAE"
S3_FOLDER = "metrics"

AWS_ACCESS_KEY = "Your_Access_Key"
AWS_SECRET_KEY = "Your_Secret_Key"
AWS_REGION = "Your_Region"

# =============================
# Collect Metrics
# =============================
def collect_metrics():
    server_name = socket.gethostname()

    metrics = {
        "timestamp": datetime.now(UTC).isoformat(),
        "server_name": server_name,
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "network_bytes_sent": psutil.net_io_counters().bytes_sent,
        "network_bytes_received": psutil.net_io_counters().bytes_recv,
        "application_errors": 0
    }

    return metrics


# =============================
# Save Metrics Locally
# =============================
def save_metrics(metrics):

    file_name = f"{metrics['server_name']}_{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}.json"

    with open(file_name, "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Metrics saved locally: {file_name}")

    return file_name


# =============================
# Upload to S3
# =============================
def upload_to_s3(file_name):

    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )

        s3.upload_file(
            file_name,
            BUCKET_NAME,
            f"{S3_FOLDER}/{file_name}"
        )

        print("Metrics uploaded to S3 successfully.")

    except ClientError as e:
        print("Upload failed:", e)


# =============================
# Main Execution
# =============================
def main():

    metrics = collect_metrics()

    print("\nCollected Metrics:")
    print(json.dumps(metrics, indent=2))

    file_name = save_metrics(metrics)

    upload_to_s3(file_name)


# Run Script
if __name__ == "__main__":
    main()