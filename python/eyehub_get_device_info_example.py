#!/usr/bin/python
# Simple example script to retrieve the details of the device
# named in DEVICE_ID using the EyeHub API

import requests
from requests.auth import HTTPBasicAuth
import json

# Change these to match your account and device details
EYEHUB_USERNAME="YOUR_EYEHUB_USERNAME"
EYEHUB_PASSWORD="YOUR_EYEHUB_PASSWORD"
DEVICE_MANAGER_ID="YOUR_DEVICE_MANAGER_ID"
DEVICE_ID="YOUR_DEVICE_ID"

# First off, let's get the basic info for the device
print "Get basic device info for %s" % DEVICE_ID

url = "http://config28.flexeye.com/v1/iot_Default/dms/%s/devices/%s" % (DEVICE_MANAGER_ID, DEVICE_ID)

# Post to the URL after encoding the dictionary as json
response = requests.get(url, auth=(EYEHUB_USERNAME, EYEHUB_PASSWORD))

if response.status_code == 200:
    # Load response content into a dict from json
    response_data = json.loads(response.content)
    # And just output the ID and number of events for now
    print "Device ID: %s" % response_data['id']
    print "Display Name: %s" % response_data['displayName']
    print "Event count: %i" % response_data['numEventsAll']
else:
    print response.status_code
    print response

