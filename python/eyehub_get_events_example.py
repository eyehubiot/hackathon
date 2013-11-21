#!/usr/bin/python
# Simple example script to retrieve the events for the device
# named in DEVICE_ID using the EyeHub API

import requests
from requests.auth import HTTPBasicAuth
import json

# Change these to match your account and device details
EYEHUB_USERNAME="YOUR_EYEHUB_USERNAME"
EYEHUB_PASSWORD="YOUR_EYEHUB_PASSWORD"
DEVICE_MANAGER_ID="DEVICE_MANAGER_ID_FOR_DEVICE_IN_DEVICE_ID"
DEVICE_ID="YOUR_DEVICE_ID"

print "Retrieving a list of events..."

url = "https://config28.flexeye.com/v1/iot_Default/dms/%s/devices/%s/events" % (DEVICE_MANAGER_ID, DEVICE_ID)

# Post to the URL after encoding the dictionary as json
response = requests.get(url, auth=(EYEHUB_USERNAME, EYEHUB_PASSWORD))

if response.status_code == 200:
    # Load response content into a dict from json
    response_data = json.loads(response.content)
    print "Number of events found: %i" % len(response_data['events'])
    for ev in response_data['events']:
        print ev['uri']
else:
    print response.status_code
    print response

