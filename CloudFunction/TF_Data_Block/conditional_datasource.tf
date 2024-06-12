data "google_cloudfunctions2_function" "gen2_cf_conditional" {
#   count = var.project_id == "some-random" ? 1 : 0 # Forcefully making it false
  count = var.project_id == "proud-climber-421817" ? 1 : 0 # making it true
  name = "cloudFunction_viaTerraform"
  project = var.project_id
  location = var.region
}

# output "gen2_cf_conditional_serviceConfig_uri" {
#   value = data.google_cloudfunctions2_function.gen2_cf_conditional.service_config[0].uri
# }

# output "gen2_cf_conditional_serviceConfig_email" {
#   value = data.google_cloudfunctions2_function.gen2_cf_conditional.service_config[0].service_account_email
# }


output "gen2_cf_conditional_serviceConfig_uri" {
  value = length(data.google_cloudfunctions2_function.gen2_cf_conditional) > 0 ? data.google_cloudfunctions2_function.gen2_cf_conditional[0].service_config[0].uri : ""
}

output "gen2_cf_conditional_serviceConfig_email" {
  value = length(data.google_cloudfunctions2_function.gen2_cf_conditional) > 0 ? data.google_cloudfunctions2_function.gen2_cf_conditional[0].service_config[0].service_account_email : ""
}
