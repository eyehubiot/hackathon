#!/usr/bin/ruby
# Simple example script to retrieve the details of the event
# named in EVENT_ID using the EyeHub API

require 'rubygems'
require 'json'
require 'net/https'

# Change these to match your account, device and event details
EYEHUB_USERNAME="YOUR_EYEHUB_USERNAME"
EYEHUB_PASSWORD="YOUR_EYEHUB_PASSWORD"
DEVICE_MANAGER_ID="DEVICE_MANAGER_ID"
DEVICE_ID="YOUR_DEVICE_ID"
EVENT_ID="YOUR_EVENT_ID"

# First off, let's get the basic info for the event
puts "Get all event info for #{DEVICE_ID}'s event #{EVENT_ID}"
device_uri = URI.parse("https://config28.flexeye.com/v1/iot_Default/dms/#{DEVICE_MANAGER_ID}/devices/#{DEVICE_ID}/events/#{EVENT_ID}")
http = Net::HTTP.new(device_uri.host, device_uri.port)
http.use_ssl = true
request = Net::HTTP::Get.new(device_uri.request_uri)
request.basic_auth(EYEHUB_USERNAME, EYEHUB_PASSWORD)
device_data = http.request(request)
# We've got a chunk of JSON data in response, so parse it to let us extract
# some useful bits
device_details = JSON.parse(device_data.body)
# Although the data are now available - just output a dump for now
puts "All Event Info: " + device_details.to_s
puts


