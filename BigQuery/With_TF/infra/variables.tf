variable "datasets" {

}

variable "view_query" {
  description = "The SQL query for the view."
  type        = string
}

variable "target_dataset_key" {
  description = "The key of the dataset to output."
  type        = string
}