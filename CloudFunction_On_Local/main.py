import os
import json
from faker import Faker
from google.cloud import pubsub_v1
from flask import Flask, request

app = Flask(__name__)
publisher = pubsub_v1.PublisherClient()
topic_name = os.getenv('PUBSUB_TOPIC')

fake = Faker()

@app.route('/', methods=['POST'])
def generate_data():
    fake_data = {
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    }

    message_json = json.dumps(fake_data)
    message_bytes = message_json.encode('utf-8')

    try:
        future = publisher.publish(topic_name, data=message_bytes)
        future.result()
        return 'Message published.', 200
    except Exception as e:
        print(e)
        return 'Error publishing message.', 500

if __name__ == '__main__':
    app.run(debug=True)
