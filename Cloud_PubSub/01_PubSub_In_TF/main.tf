resource "google_pubsub_topic" "cloud_pubsub_topic_tf" {
  name    = "pubsub_topic_tf"
  project = var.project-id
  labels = {
    foo = "bar"
  }
  message_retention_duration = "86600s"
}
# Initially I have provided code as "project    = "${var.project-id}"", hwoever with the run of terraform fmt this is changed to project = var.project-id 

resource "google_pubsub_subscription" "cloud_pubsub_sub_tf" {
  name                       = "pubsub_sub_tf"
  topic                      = google_pubsub_topic.cloud_pubsub_topic_tf.name
  project                    = var.project-id
  message_retention_duration = "1200s"
  retain_acked_messages      = true
  ack_deadline_seconds       = 20
}