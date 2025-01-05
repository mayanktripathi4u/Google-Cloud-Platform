from google.cloud import resourcemanager_v3
from google.cloud import iam_v1

def collect_iam_data(project_id):
    client = resourcemanager_v3.ProjectsClient()
    iam_policy = client.get_iam_policy(request={"resource": f"projects/{project_id}"})
    
    # Process and return the IAM policy data
    return iam_policy

# Collect data from multiple projects
projects = ["project-1", "project-2", "project-3"]
iam_data = [collect_iam_data(project) for project in projects]

