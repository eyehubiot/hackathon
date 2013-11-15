#!/usr/bin/python
# Simple example script to generate an event from the device
# named in DEVICE_ID using the EyeHub API

import requests
from requests.auth import HTTPBasicAuth
import json

# Change these to match your account and device details
EYEHUB_USERNAME="YOUR_EYEHUB_USERNAME"
EYEHUB_PASSWORD="YOUR_EYEHUB_PASSWORD"
DEVICE_MANAGER_ID="DEVICE_MANAGER_ID_FOR_DEVICE_IN_DEVICE_ID"
DEVICE_ID="YOUR_DEVICE_ID"

print "Creating a new event..."

url = "https://config28.flexeye.com/v1/iot_Default/dms/%s/devices/%s/events" % (DEVICE_MANAGER_ID, DEVICE_ID)
# These are the event parameters
data = { 'source': 'test_sensor', 'type': '1.0', 'payload': '123' }
headers = { 'Content-Type': 'application/json' }

# Post to the URL after encoding the dictionary as json
response = requests.post(url, auth=(EYEHUB_USERNAME, EYEHUB_PASSWORD), data=json.dumps(data), headers=headers)

if response.status_code == 201:
    # Load response content into a dict from json
    response_data = json.loads(response.content)
    print "Created."
else:
    print "Failed to create event"
    print response.status_code
    print response
