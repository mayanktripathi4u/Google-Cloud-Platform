import base64
import functions_framework 

# Trigger from a message on a Cloud Pub/Sub Topic
@functions_framework.cloud_event
def trigger_by_pubsub(cloud_event):
    # Print out data from Pub/Sub Topic
    print(base64.b64decode(cloud_event.data["message"]["data"]))