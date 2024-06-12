terraform {
  backend "gcs" {
    bucket = "gcp_terraform_state_files" # Bucket
    prefix = "GH_GCP_PUBSUB_TF"          # Folder
  }

  required_providers {
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 4.44.1"
    }
  }
}