def fileUpload(event, context):
    file_data = event

    # Extract relevant information from the event
    bucket_name = file_data['bucket']
    file_name = file_data['name']
    file_size = file_data['size']

    # Perform desired operations on the uploaded file
    # For example, you can process the file, store metadata, or trigger other actions

    print(f"File uploaded: {file_name} in bucket: {bucket_name}")
    print(f"File size: {file_size} bytes")

    print('Event ID:' , context.event_id)
    print('Event type:', context.event_type)
    print('Bucket:', event['bucket'])
    print('File:',  event['name'])
    print('Metageneration:',  event['metageneration'])
    print('Created:',  event['timeCreated'])
    print('Updated:',  event['updated'])

    # Add your custom logic here

    # Return a response (optional)
    return "File processing completed"