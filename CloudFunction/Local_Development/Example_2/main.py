import functions_framework

@functions_framework.cloud_event
def hello(event, context):
     print("hello cloud function called.")
     print("Received", context.event_id)