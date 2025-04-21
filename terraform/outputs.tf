output "pubsub_topic" {
  value = google_pubsub_topic.bart_etd.name
}

output "bigquery_table_id" {
  value = google_bigquery_table.bart_etd_table.table_id
}
