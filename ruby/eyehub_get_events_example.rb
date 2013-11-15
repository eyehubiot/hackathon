#!/usr/bin/ruby
# Simple example script to retrieve the events for the device
# named in DEVICE_ID using the EyeHub API

require 'rubygems'
require 'json'
require 'net/https'

# Change these to match your account and device details
EYEHUB_USERNAME="YOUR_EYEHUB_USERNAME"
EYEHUB_PASSWORD="YOUR_EYEHUB_PASSWORD"
DEVICE_MANAGER_ID="DEVICE_MANAGER_ID"
DEVICE_ID="YOUR_DEVICE_ID"

# Now let's get a list of just the events
puts "Retrieving a list of events..."
event_uri = URI.parse("https://config28.flexeye.com/v1/iot_Default/dms/#{DEVICE_MANAGER_ID}/devices/#{DEVICE_ID}/events")
http = Net::HTTP.new(event_uri.host, event_uri.port)
http.use_ssl = true
request = Net::HTTP::Get.new(event_uri.request_uri)
request.basic_auth(EYEHUB_USERNAME, EYEHUB_PASSWORD)
event_data = http.request(request)
# Again, the response will be formatted in JSON
event_details = JSON.parse(event_data.body)
puts "Number of events found: "+event_details["events"].count.to_s
# And output some info for each event we found
event_details["events"].each do |ev|
  puts ev["uri"]
end
puts

