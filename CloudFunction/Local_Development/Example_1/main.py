from google.cloud import pubsub_v1
# import os
from functions_framework import cloud_event
import base64

# Cloud Function triggered by Pub/Sub
"""
The @cloud_event decorator (from the functions-framework) tells the framework that this function should be invoked when an event occurs.

You can access the message through cloud_event.data, where it will be in base64 encoded form. We decode it here using message_data.decode('utf-8').
"""
@cloud_event
def my_function(cloud_event):
    """Triggered by a Pub/Sub message."""
    print(f"Google Cloud Function : {my_function} called.")

    pubsub_message = cloud_event.data['message']['data']

    print(f"Message Received (Before Decoding) : {pubsub_message}")
    
    if pubsub_message:
        # message = pubsub_message.decode('utf-8')

        # If you're receiving the message as base64-encoded, decode it
        message = base64.b64decode(pubsub_message).decode('utf-8')

        print(f"Received message: {message}")
        # Add your function logic here (e.g., send a message to another Pub/Sub topic)
    else:
        print("No Message Received to the CF. Re-Try!!!")