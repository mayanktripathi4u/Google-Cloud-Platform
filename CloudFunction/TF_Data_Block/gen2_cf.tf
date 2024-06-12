data "google_cloudfunctions2_function" "gen2_cloud_function" {
  name = "cloudFunction_viaTerraform"
  project = var.project_id
  location = var.region
}

# Output in given Order. 
# https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloudfunctions2_function

output "cloud_function_v2_buildconfig" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.build_config
}

output "cloud_function_v2_desc" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.description
}

output "cloud_function_v2_env" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.environment
}

output "cloud_function_v2_eventTrigger" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.event_trigger
}

output "cloud_function_v2_id" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.id
}

output "cloud_function_v2_labels" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.labels
}

output "cloud_function_v2_loc" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.location
}

output "cloud_function_v2_name" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.name
}

output "cloud_function_v2_prj" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.project
}

output "cloud_function_v2_serviceConfig" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.service_config
}

output "cloud_function_v2_serviceConfig_uri" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.service_config[0].uri
}

output "cloud_function_v2_serviceConfig_email" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.service_config[0].service_account_email
}

output "cloud_function_v2_state" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.state
}

output "cloud_function_v2_updtTime" {
  value = data.google_cloudfunctions2_function.gen2_cloud_function.update_time
}













