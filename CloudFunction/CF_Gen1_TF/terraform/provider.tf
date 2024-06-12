# terraform {
#   required_version = ">= 1.0"
#   required_providers {
#     google = {
#       source  = "hashicorp/google"
#       version = "~> 4.69.1"
#     }
#   }
# }

terraform {
  backend "gcs" {
    bucket = "gcp_terraform_state_files" # Bucket
    prefix = "GH_GCP_CF_TF_Gen1"         # Folder
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