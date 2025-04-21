provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_pubsub_topic" "bart_etd" {
  name = "bart-etd"
}

resource "google_bigquery_dataset" "bart_dataset" {
  dataset_id = "bart_data"
  location   = var.region
}

resource "google_bigquery_table" "bart_etd_table" {
  dataset_id = google_bigquery_dataset.bart_dataset.dataset_id
  table_id   = "bart_etd"
  schema     = file("${path.module}/bart_etd_schema.json")
  time_partitioning {
    type = "DAY"
  }
}

resource "google_service_account" "dataflow_sa" {
  account_id   = "dataflow-service"
  display_name = "Dataflow Service Account"
}

resource "google_project_iam_member" "dataflow_pubsub" {
  role   = "roles/pubsub.subscriber"
  member = "serviceAccount:${google_service_account.dataflow_sa.email}"
}

resource "google_project_iam_member" "dataflow_bigquery" {
  role   = "roles/bigquery.dataEditor"
  member = "serviceAccount:${google_service_account.dataflow_sa.email}"
}
