data "google_cloudfunctions_function" "gen1_cloud_function" {
  name    = "trigger-dataflow-job"
  project = var.project_id
  region  = var.region
}

# All output from https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloudfunctions_function

output "output_gen1_cf_name" {
  value = data.google_cloudfunctions_function.gen1_cloud_function.name
}


output "output_gen1_cf_kms" {
  value = data.google_cloudfunctions_function.gen1_cloud_function.kms_key_name
}

output "output_gen1_cf_url" {
    description = "Output for Gen 1 Cloud Function - Get the URI"
  value = data.google_cloudfunctions_function.gen1_cloud_function.https_trigger_url
}

output "output_gen1_cf_trigger" {
    description = "Output for Gen 1 Cloud Function -  If function is triggered by HTTP, this boolean is set."
  value = data.google_cloudfunctions_function.gen1_cloud_function.trigger_http
}

output "output_gen1_cf_serviceemail" {
  value = data.google_cloudfunctions_function.gen1_cloud_function.service_account_email
}
