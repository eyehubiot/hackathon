#!/usr/bin/python
# Simple example script to retrieve the events for the device
# named in DEVICE_ID using the EyeHub API

import requests
from requests.auth import HTTPBasicAuth
import json

# Change these to match your account and device details
EYEHUB_USERNAME="orders2008@sheerman-chase.org.uk"
EYEHUB_PASSWORD="testtim"
DEVICE_MANAGER_ID="CCSR_DM"
DEVICE_ID="TimBB"
EVENT_ID="38446"

print "Retrieving event %s..." % (EVENT_ID,)

url = "https://config28.flexeye.com/v1/iot_Default/dms/%s/devices/%s/events/%s" % (DEVICE_MANAGER_ID, DEVICE_ID, EVENT_ID)

# Post to the URL after encoding the dictionary as json
response = requests.get(url, auth=(EYEHUB_USERNAME, EYEHUB_PASSWORD))

if response.status_code == 200:
    # Load response content into a dict from json
    response_data = json.loads(response.content)
    for k in response_data:
		print k, response_data[k]
else:
    print response.status_code
    print response

