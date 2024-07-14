provider "google" {
  project = "proud-climber-421817"
  region  = "us-central1"
}

# Create GCS bucket for CSV files
resource "google_storage_bucket" "bucket" {
  name     = "cloud-metric-tracker"
  location = "US"
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = "cloud_metrics"
  location   = "US"
}

resource "google_bigquery_table" "table" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = "raw_cloud_metrics"

  schema = file("schemas/bq_schema.json")
}

resource "google_bigquery_table" "table2" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = "final_cloud_metrics"

  schema = file("schemas/bq_schema2.json")
}

# Create GCS bucket for Cloud Function source code
resource "google_storage_bucket" "cf_bucket" {
  name     = "cf_source_code_06july_mt"
  location = "US"
}

# Create archive from function files
resource "null_resource" "zip_function" {
  provisioner "local-exec" {
    command = "cd functions && zip -r function-source.zip main.py requirements.txt"
  }
}

# Upload zip file to GCS
resource "google_storage_bucket_object" "function_zip" {
  name   = "cloud-metric-tracker/function-source.zip"
  source = "functions/function-source.zip"
  bucket = google_storage_bucket.cf_bucket.name

  depends_on = [null_resource.zip_function]
}

# Deploy Cloud Function
resource "google_cloudfunctions_function" "function" {
  name        = "csv_to_bigquery"
  description = "Triggered by GCS, processes CSV and loads into BigQuery"
  runtime     = "python310"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.cf_bucket.name
  source_archive_object = google_storage_bucket_object.function_zip.name
  entry_point           = "process_csv"

  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = google_storage_bucket.bucket.name
  }

  environment_variables = {
    BQ_DATASET           = google_bigquery_dataset.dataset.dataset_id
    BQ_TABLE             = google_bigquery_table.table.table_id
    GOOGLE_CLOUD_PROJECT = var.PROJECT_ID

  }
}

# resource "google_storage_bucket_object" "main_py" {
#   name   = "main.py"
#   source = "functions/main.py"
#   bucket = google_storage_bucket.bucket.name
# }

# resource "google_storage_bucket_object" "requirements_txt" {
#   name   = "requirements.txt"
#   source = "functions/requirements.txt"
#   bucket = google_storage_bucket.bucket.name
# }

# resource "google_cloudfunctions_function" "function" {
#   name        = "csv_to_bigquery"
#   description = "Triggered by GCS, processes CSV and loads into BigQuery"
#   runtime     = "python310"

#   available_memory_mb   = 256
#   source_archive_bucket = google_storage_bucket.bucket.name
#   source_archive_object = google_storage_bucket_object.main_py.name
#   entry_point           = "process_csv"

#   event_trigger {
#     event_type = "google.storage.object.finalize"
#     resource   = google_storage_bucket.bucket.name
#   }

#   environment_variables = {
#     BQ_DATASET = google_bigquery_dataset.dataset.dataset_id
#     BQ_TABLE   = google_bigquery_table.table.table_id
#   }
# }
