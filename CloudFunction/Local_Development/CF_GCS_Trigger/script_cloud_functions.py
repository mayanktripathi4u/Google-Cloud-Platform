import functions_framework
from cloudevents.http import CloudEvent

# This function processes Audit Log event for storage.object.create
@functions_framework.cloud_event
def hello_gcs(cloud_event: CloudEvent) -> None:
    """This function is triggered by a change in a storage bucket.

    Args:
        cloud_event: The CloudEvent that triggered this function.
    Returns:
        None
    """
    resource_name = cloud_event.data["protoPayload"]["resourceName"]
    print(resource_name)