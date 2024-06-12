resource "google_storage_bucket" "Cloud_function_bucket" {
  name     = "cloud-function-${var.project_id}"
  location = var.region
  project  = var.project_id
}

resource "google_storage_bucket" "input_bucket" {
  name     = "input-${var.project_id}"
  location = var.region
  project  = var.project_id
}