provider "google" {
  project = var.project_id
  region  = "us-central1"
}

resource "google_storage_bucket" "dataflow_bucket" {
  name          = "dataflow-job-${var.project_id}"
  location      = "US"
  force_destroy = true
}

resource "google_pubsub_topic" "input_topic" {
  name = "input-topic"
}

resource "google_pubsub_subscription" "input_subscription" {
  name  = "input-subscription"
  topic = google_pubsub_topic.input_topic.name
}

resource "google_dataflow_job" "streaming_job" {
  name             = "streaming-uppercase-job"
  template_gcs_path = "gs://your-dataflow-bucket/templates/uppercase-template"
  parameters = {
    input_subscription = "projects/your-gcp-project-id/subscriptions/input-subscription"
    output_path        = "gs://your-dataflow-bucket/output/"
  }
  on_delete        = "cancel"
  zone             = "us-central1-f"
}

output "dataflow_job_name" {
  value = google_dataflow_job.streaming_job.name
}
