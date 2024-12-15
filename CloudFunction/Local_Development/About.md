# Cloud Function - Local Development and Testing
Google Cloud Functions, especially Gen 1 functions, can be tested locally using frameworks like the `Functions Framework`. It allows you to run and test Google Cloud Functions locally, mimicking the Cloud Functions environment without needing to deploy them first. Here's a step-by-step guide to help you develop and test your Google Cloud Function locally, specifically for a Pub/Sub trigger using the Functions Framework.

## Prerequisites
1. Google Cloud SDK: Make sure you have the Google Cloud SDK installed and authenticated.
2. Node.js or Python: Depending on your runtime (Node.js or Python), install the appropriate version.
3. Docker (optional): For more complex use cases or running the function in an isolated environment, Docker is helpful.
4. Google Cloud Pub/Sub emulator: If you're simulating a Pub/Sub trigger locally, the Pub/Sub emulator is a good tool to use.


## Steps:
1. Set up your local environment

Make sure your environment has the required tools installed.
   * Python (for Python runtime):
```bash
sudo apt-get install python3 python3-pip
```
   * Install Google Cloud SDK if not already done:
```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
```
   * Install Docker (optional, if needed for a more isolated environment).
   * Install the Functions Framework --> The Functions Framework provides a way to run Cloud Functions locally. Choose the one for your runtime.
```bash
pip install functions-framework
```

2. Create Your Cloud Function
   * You can create a Pub/Sub-triggered function. [Source Code](/Google-Cloud-Platform/CloudFunction/Local_Development/Example_1/main.py)
   * Install Dependencies
```bash
pip install -r requirements.txt
```

3. Test Locally
   * You can start the function locally by running the following command:
```bash
functions-framework --target=my_function
```

4. Install and configure Google Cloud Pub/Sub Emulator
   * To test your function with a real Pub/Sub trigger locally, you can use the Google Cloud Pub/Sub Emulator.
   * Install Pub/Sub Emulator: (use Terminal-1)
```bash
gcloud components install pubsub-emulator
```
   * Start the Pub/Sub emulator: (use Terminal-1)
    After running the command gcloud beta emulators pubsub start, the emulator is active and listening for requests. At this point, Terminal-1 won’t accept any additional commands. It's now just processing the emulator and logging messages like [pubsub] INFO: Server started, listening on 8606.
```bash
gcloud beta emulators pubsub start
```
   * Set the environment variables to point to the emulator: (use Terminal-2)
```bash
export PUBSUB_EMULATOR_HOST=localhost:8085

# Now, check if the environment variable is set:
echo $PUBSUB_EMULATOR_HOST

```
    This ensures your code will interact with the local Pub/Sub emulator instead of the real Google Cloud service.
   * Create a topic and subscription: In another terminal, use the emulator's command line to create a topic and subscription
```bash
# Create the topic
gcloud pubsub topics create test_topic_emulator

gcloud pubsub subscriptions create test_subscription_emulator --topic test_topic_emulator

```
5. Test the Cloud Function locally
   Now that you have everything set up, you can test the function locally.
   * Start your function locally:
```bash
functions-framework --target=my_function

# run the function on port 8081:
functions-framework --target=my_function --port=8081

```
   * Publish a test message to the Pub/Sub topic:
```bash
gcloud pubsub topics publish test_topic_emulator --message "Hello, Cloud Function!"

gcloud pubsub topics publish test_topic_emulator --message "Hello, this is a test message!"

```

6. Deploy to Google Cloud
   Once you've tested everything locally, you're ready to deploy the function to Google Cloud:
```bash
gcloud functions deploy my_function \
  --runtime python39 \
  --trigger-topic test_topic_emulator
```


```bash
sudo lsof -i :8081 
kill -9 <pid>
```

# How to test
[Test locally with the Pub/Sub emulator](https://cloud.google.com/functions/docs/local-development)

Test this feature as described here. Note that it requires you to use three separate terminal instances:
1. In the first terminal, start the Pub/Sub emulator on port 8043 in a local project:
```bash
gcloud beta emulators pubsub start \
    --project=gcphde-prim-dev-data \
    --host-port='localhost:8043'
```
2. In the second terminal, create a Pub/Sub topic and subscription:
```bash
curl -s -X PUT 'http://localhost:8043/v1/projects/gcphde-prim-dev-data/topics/sample-topic-emu'
```
Use http://localhost:8080 as the push subscription's endpoint.
```bash
curl -s -X PUT 'http://localhost:8043/v1/projects/gcphde-prim-dev-data/subscriptions/mysub' \
    -H 'Content-Type: application/json' \
    --data '{"topic":"projects/gcphde-prim-dev-data/topics/sample-topic-emu","pushConfig":{"pushEndpoint":"http://localhost:8080/projects/gcphde-prim-dev-data/topics/sample-topic-emu"}}'
```
3. In the third terminal, clone the sample repository to your local machine:
   * Write Cloud Function (Already Done)
   * Create the buildpack (this may take a few minutes):
```bash
pack build \
  --builder gcr.io/buildpacks/builder:v1 \
  --env GOOGLE_FUNCTION_SIGNATURE_TYPE=event \
  --env GOOGLE_FUNCTION_TARGET=subscribe \
  my-function
```
   * Start the Pub/Sub function on port 8080. This is where the emulator will send push messages:
```bash
docker run --rm -p 8080:8080 my-function
```
   * In the second terminal, invoke the function by publishing a message. The message data needs to be encoded in base64. This example uses the base64 encoded string {"foo":"bar"}.
```bash
curl -s -X POST 'http://localhost:8043/v1/projects/gcphde-prim-dev-data/topics/sample-topic-emu:publish' \
    -H 'Content-Type: application/json' \
    --data '{"messages":[{"data":"eyJmb28iOiJiYXIifQ=="}]}'
```



# Logging
To determine how and when the Pub/Sub topic was created, you need to gather information about its creation and any changes to the topic.

Below will give all pub/sub topics (limiting to 2 in the example.)
```bash
gcloud logging read 'resource.type="pubsub_topic"' --limit 2
```

Below will filter for all topics which got created.
```bash
gcloud logging read 'resource.type="pubsub_topic" AND protoPayload.authorizationInfo.permission="pubsub.topics.create"' --limit 2
```

Below will filter for published messages
```bash
gcloud logging read 'resource.type="pubsub_topic" AND protoPayload.methodName=~"Publisher.Publish"' --limit 2
```
