<img width="741" height="861" alt="Architectural drawing" src="https://github.com/user-attachments/assets/4543141a-b93b-4ce2-8274-7c5f2a2687d6" />

# 🚀 CloudPulse: Advanced Infrastructure Observability Platform

CloudPulse is a real-world cloud monitoring system that collects server metrics, detects anomalies, and sends real-time alerts using AWS services.


---

## 📌 Project Overview
This project simulates a **production-grade observability pipeline**:

* Collect system metrics (CPU, memory, disk, network)
* Store metrics in cloud storage
* Automatically detect anomalies
* Send email alerts when thresholds are exceeded

---

## 🏗️ Architecture

```
Python Monitoring Script
        ↓
Amazon S3 (metrics storage)
        ↓
AWS Lambda (anomaly detection)
        ↓
Amazon SNS (email alerts)
```

---

## ⚙️ Technologies Used

* Python (psutil, boto3)
* AWS S3
* AWS Lambda
* AWS SNS
* AWS IAM
* Amazon CloudWatch (logs)

---

## 📂 Project Structure

```
cloudpulse-observability/
│
├── monitoring_script/
│   └── monitoring.py
│
├── lambda_function/
│   └── lambda_function.py
│
├── test_data/
│   └── test_alert_metrics.json
│
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/cloudpulse-observability.git
cd cloudpulse-observability
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure AWS Credentials

```bash
aws configure
```

Provide:

* AWS Access Key
* AWS Secret Key
* Region (e.g. us-east-1)

---

### 4️⃣ Create S3 Bucket

* Name: `Your_BUCKET_NAME`
* Create folder: `metrics/`

---

### 5️⃣ Create SNS Topic

* Topic name: `server-alerts-topic`
* Add email subscription and confirm it

---

### 6️⃣ Deploy Lambda Function

* Runtime: Python 3.x
* Attach permissions:

  * S3 Read Access
  * SNS Publish Access
* Add S3 trigger:

  * Prefix: `metrics/`
  * Suffix: `.json`

---

## 🧪 Testing the System

Upload test data:

```bash
aws s3 cp test_data/test_alert_metrics.json s3://kafui-network-monitor-storage/metrics/
```

---

## 📊 Sample Metrics

```json
{
  "timestamp": "2026-03-16T10:30:00Z",
  "server_name": "test-server",
  "cpu_usage_percent": 95,
  "memory_usage_percent": 90,
  "disk_usage_percent": 50
}
```

---

## 🚨 Expected Output

If thresholds are exceeded:

* CPU > 80%
* Memory > 85%
* Disk > 90%

📩 You will receive an email alert via SNS.
![AlertMessage](https://github.com/user-attachments/assets/3dba1c72-82bd-4f52-91a8-90bcc1c63cff)


---

## 🔍 Key Features

✅ Real-time monitoring
✅ Serverless anomaly detection
✅ Automated alerting system
✅ Scalable cloud architecture
✅ Production-style design

---

## 💡 Future Improvements

* Add dashboard (AWS QuickSight / Grafana)
* Integrate AI anomaly detection
* Store data in Amazon RDS / DynamoDB
* Add API Gateway for real-time ingestion

---

## 👨‍💻 Author

**Daniel Afeamenyo**

* Cloud & Machine Learning Engineer
* Passionate about building scalable cloud solutions

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share on LinkedIn
* Fork and improve it

---

