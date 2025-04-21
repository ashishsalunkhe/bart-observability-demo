# 🚦 BART Real-Time Observability Pipeline (GCP + OpenTelemetry)

A production-grade, real-time data engineering project that streams Bay Area Rapid Transit (BART) train data, processes it using GCP-native services, and adds deep observability using OpenTelemetry, Prometheus, Grafana, and Jaeger.

## 🗂️ Project Structure

```
📁 bart-observability-pipeline/
├── README.md
├── terraform/                        # Infra-as-code for GCP resources
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── cloud-functions/
│   └── ingest_bart_etd/             # Cloud Function to fetch and publish BART ETD
│       ├── main.py
│       └── requirements.txt
├── dataflow/
│   └── streaming_pipeline/
│       ├── pipeline.py              # Apache Beam pipeline
│       ├── pipeline_utils.py
│       └── requirements.txt
├── observability/
│   ├── otel-collector-config.yaml   # OpenTelemetry Collector config
│   ├── grafana-dashboards/
│   └── prometheus-rules.yaml        # Alerting rules
├── bigquery/
│   └── schemas/
│       └── bart_etd_schema.json
├── dbt/
│   └── models/                      # Optional if using dbt for transformations
├── docs/
│   ├── architecture-diagram.png
│   └── lineage-overview.md
└── scripts/
    └── test_replay_pubsub.py        # Replay tool for testing
```

---

## 🛠️ Tech Stack

- **Ingestion**: Cloud Scheduler + Cloud Functions + Pub/Sub
- **Processing**: Dataflow (Apache Beam)
- **Storage**: BigQuery, Cloud Storage (Parquet)
- **Observability**: OpenTelemetry, Prometheus, Jaeger, Grafana
- **Security**: IAM roles, service accounts, CMEK (optional)
- **CI/CD**: Terraform + GitHub Actions (to be added)

---

## 📈 Features

- 🚆 Real-time ingestion of BART train data
- ⚙️ Streaming transformation with Dataflow
- 🔍 End-to-end observability with OpenTelemetry
- 📦 Metrics export to Prometheus and traces to Jaeger/Cloud Trace
- 📊 Grafana dashboards for latency, lag, and throughput
- 🧪 Alerting on data freshness or pipeline issues
- 🔁 Replay and backfill support
- 🧰 Schema registry + data validation (optional Avro/Protobuf)

---

## 🚀 Getting Started

### Prerequisites
- GCP account with billing enabled
- Enable APIs: Pub/Sub, Cloud Functions, Dataflow, BigQuery, Cloud Monitoring
- Python 3.8+

### Setup
```bash
# Clone the repo
$ git clone https://github.com/yourusername/bart-observability-pipeline.git
$ cd bart-observability-pipeline

# Deploy infra
$ cd terraform && terraform init && terraform apply

# Deploy Cloud Function
$ cd ../cloud-functions/ingest_bart_etd
$ gcloud functions deploy fetch_bart_etd --runtime python310 \
    --trigger-topic bart-etd --entry-point fetch_bart_etd

# Run Dataflow Job (Template or Direct Run)
$ python pipeline.py --runner=DataflowRunner ...
```

---

## 🔒 Security Best Practices
- Use Workload Identity Federation
- Assign least-privilege roles to each component
- Optionally enable CMEK for GCS + BQ

---

## 📊 Observability Setup
- Deploy OpenTelemetry Collector on Cloud Run
- Configure Grafana to pull from Prometheus + Jaeger
- Use dashboards in `/observability/grafana-dashboards/`

---

## 📚 Resources
- [BART API Docs](https://api.bart.gov/docs/etd/)
- [OpenTelemetry](https://opentelemetry.io/docs/)
- [Apache Beam](https://beam.apache.org/)
- [GCP Dataflow](https://cloud.google.com/dataflow)

---

## 📌 TODOs
- [ ] Add dbt models for analytical use cases
- [ ] Add GitHub Actions CI/CD pipeline
- [ ] Add Looker Studio dashboard examples

---

## 📄 License
MIT License

---

## 👨‍💻 Author
Ashish Salunkhe | [ashishsalunkhe.com](https://ashishsalunkhe.com) | [LinkedIn](https://linkedin.com/in/ashishsalunkhe)
