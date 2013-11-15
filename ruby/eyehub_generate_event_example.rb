#!/usr/bin/ruby
# Simple example script to generate an event from the device
# named in DEVICE_ID using the EyeHub API

require 'rubygems'
require 'json'
require 'net/https'

# Change these to match your account and device details
EYEHUB_USERNAME="YOUR_EYEHUB_USERNAME"
EYEHUB_PASSWORD="YOUR_EYEHUB_PASSWORD"
DEVICE_MANAGER_ID="DEVICE_MANAGER_ID"
DEVICE_ID="YOUR_DEVICE_ID"

puts "Creating a new event..."

# Gather the event parameters
request_params = {}
request_params["source"] = "test_sensor"
request_params["payload"] = "123"
request_params["type"] = "1.0"

# Now call the EyeHub API
event_uri = URI.parse("https://config28.flexeye.com/v1/iot_Default/dms/#{DEVICE_MANAGER_ID}/devices/#{DEVICE_ID}/events")
http = Net::HTTP.new(event_uri.host, event_uri.port)
http.use_ssl = true
request = Net::HTTP::Post.new(event_uri.request_uri)
request.basic_auth(EYEHUB_USERNAME, EYEHUB_PASSWORD)
# Add the parameters to the request, formatted as JSON
request.body = request_params.to_json
# And tell the server that the data we're sending is formatted as JSON
request["Content-Type"] = "application/json"
# Now call the server
creation_result = http.request(request)

if creation_result.kind_of? Net::HTTPSuccess
  result_info = JSON.parse(creation_result.body)
  puts "Created."
else
  puts "Failed to create event"
  puts creation_result
end
