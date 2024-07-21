
resource "google_storage_bucket" "bucket1" {
  name     = "demo-source-bkt-21july"
  project  = "proud-climber-421817"
  location = "US"
}

resource "google_storage_bucket" "bucket2" {
  name     = "demo-dest-bkt-21july"
  project  = "proud-climber-421817"
  location = "US"
}

data "archive_file" "zip-function-code" {
  type        = "zip"
  source_dir  = "./Python_Script"
  output_path = "./Python_script/index.zip"
}

resource "google_storage_bucket_object" "archive" {
  name   = "index.zip"
  bucket = google_storage_bucket.bucket1.name
  source = data.archive_file.zip-function-code.output_path
}

resource "google_cloudfunctions_function" "function" {
  project               = "proud-climber-421817"
  region                = "us-central1"
  name                  = "demo-cld-fun"
  description           = "My Cloud Function"
  runtime               = "python39"
  service_account_email = "devops-admin@proud-climber-421817.iam.gserviceaccount.com"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.bucket1.name
  source_archive_object = google_storage_bucket_object.archive.name

  entry_point = "pdf_to_excel"

  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = google_storage_bucket.bucket1.name
  }
}


# IAM Entry for a single User to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
