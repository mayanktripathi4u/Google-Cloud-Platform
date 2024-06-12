provider "google" {
  project = "proud-climber-421817"
  region  = "us-cental1"
}

locals {
  datasets = var.datasets
  tables = flatten([
    for dataset_id, tables in local.datasets : [
      for table in tables : {
        dataset_id  = dataset_id
        table_id    = table.table_id
        schema_file = table.schema_file
      }
    ]
  ])
}

resource "google_bigquery_dataset" "datasets" {
  for_each   = local.datasets
  dataset_id = each.key
}

resource "google_bigquery_table" "tables" {
  for_each   = { for table in local.tables : "${table.dataset_id}.${table.table_id}" => table }
  dataset_id = each.value.dataset_id
  table_id   = each.value.table_id
  schema     = file(each.value.schema_file)
  depends_on = [google_bigquery_dataset.datasets]
}

#  Define a BigQuery view
resource "google_bigquery_table" "view" {
  # dataset_id = var.target_dataset_key
  dataset_id = google_bigquery_dataset.datasets[var.target_dataset_key].dataset_id
  table_id   = "myViewViaTF"
  view {
    query          = var.view_query
    use_legacy_sql = false
  }
}


output "target_dataset_id" {
  description = "The ID of the specified target dataset."
  value       = google_bigquery_dataset.datasets[var.target_dataset_key].dataset_id
}

output "all_dataset_ids" {
  description = "The IDs of the created datasets."
  value       = [for key, dataset in google_bigquery_dataset.datasets : dataset.dataset_id]
}