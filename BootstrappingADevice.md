# Bootstrapping a Device

## Architectural Overview

The EyeHub service is made up of a number of different types of objects.  The [IoT Model Diagram.pdf](IoT Model Diagram.pdf) shows how they all inter-relate, but we will look at a few of the key ones here:

<dl>
  <dt>Device</dt><dd>These are the sensors or actuators which feed data in from the real world, or signal out to the real world.</dd>
  <dt>Person</dt><dd>Person objects represent the people interacting with the system.</dd>
  <dt>Location</dt><dd>These represent fixed physical locations in the real world.</dd>
  <dt>Event</dt><dd>Events provide the way for information to flow between Devices, Persons and Locations.</dd>
</dl>

Device, Person and Location objects have associated respective Manager objects, which are used to group and administer collections of those objects.

For the full API documentation, see the [TSB_IoT_EyeHub_ServiceAPI.pdf](TSB_IoT_EyeHub_ServiceAPI.pdf) file.

## Registering Your Device

The first step in hooking a device up to EyeHub is to register it with the system.

While you can do this programmatically, the easiest way for your first device is to register it manually through your web browser.

1. Log into the [EyeHub website](https://config28.flexeye.com).
1. In the top menu bar, click on "Devices".
1. Choose the Device Manager that your Device will live under. Unless you know that your device will live in an existing Device Manager, you should create a new Device Manager for your devices:
    1. Click the "Add New Device Manager" button at the bottom of the left column.
    1. Enter the ID for your new Device Manager, and click the "Submit" button.  The Device Manager lets you group Devices together logically, so choose an ID that either reflects that, or otherwise one that shows it is where all *your* Devices will live.
    1. Click on the new Device Manager in the list on the left.  You'll get an empty list of Devices on the right-hand side.
1. At the bottom of the right-hand column, click "Add New Device".
1. Enter the details for your Device:
    <dl>
      <dt>Device ID</dt><dd>The ID for your your device.</dd>
      <dt>Name</dt><dd>A human-readable name for this Device.</dd>
      <dt>Type</dt><dd>Choose "Sensor" if it only has a single sensor, otherwise "Multi-Sensor".</dd>
      <dt>Description</dt><dd>A human-readable description for the device.</dd>
    </dl>
1. Click "Submit" to create the Device.  You should see it appear in the list of devices in the right-hand column of the screen.

## Exploring The Devices With `curl`

All of the API calls use basic authentication to verify that you have the right permission to use them.  That means that usernames and passwords would be transmitted in the clear, so if you're accessing the EyeHub service across an insecure network (such as the Internet) then you should use HTTPS rather than plain HTTP.

Before we get into accessing the API with code, we'll use the `curl` network tool to exercise it from the command line.  You might need to install `curl` first, Windows users can [find it here](http://curl.haxx.se/download.html), for other systems it tends to be available from your software package manager.

We'll start by getting the state of the newly created Device, just to prove that it exists and we can access it from outside the web browser.  In a terminal or command prompt window run the following command:

    curl -u <YOUR USERNAME> https://config28.flexeye.com/v1/iot_Default/dms/<YOUR DEVICE MANAGER ID>/devices/<YOUR DEVICE ID>

You will be prompted to enter your password, and then (assuming all goes to plan) you should see a chunk of JSON-formatted data printed out, with the details of the Device you created earlier.

That call is a simple GET request, to retrieve the data about the Device.  We can make a similar call to get a list of all the events for the Device:

    curl -u <YOUR USERNAME> https://config28.flexeye.com/v1/iot_Default/dms/<YOUR DEVICE MANAGER ID>/devices/<YOUR DEVICE ID>/events

If you try that now, you'll likely get an empty set of results.  We can fix that by generating an event:

    curl -u <YOUR USERNAME> -X POST -d "{\"payload\":\"123\", \"type\":\"1.0\", \"id\":\"MCQN_Test1\" }" -H "Content-Type: application/json" https://config28.flexeye.com/v1/iot_Default/dms/<YOUR DEVICE MANAGER ID>/devices/<YOUR DEVICE ID>/events

That passes a number of parameters, formatted as JSON - the string following the `--data-binary` parameter - into a POST request to the Device's events URL.  Because we're sending data formatted as JSON we need to tell the EyeHub server, which is what happens with the `-H` parameter.

If all goes well you should get a chunk of detailed JSON data in response, containing all of the information about the Event that you just created.

## Talking to the API from Ruby or Python

We have some example scripts to show how to call the API in two of the more popular scripting languages: Ruby and Python.

To use the Ruby scripts, you'll need to have the `json` gem installed.  If you don't have it already, it should be easy to install with `gem install json`.

To use the Python scripts, you'll need the `requests` module installed.  If you don't already have it, it should be easy to install with `pip install requests`

## Hardware Hacking with Arduino

For Arduino-hackers, we have example sketches which will generate events in the system.  At present the event details are hard-coded, but that can be modified for whatever data you are gathering.  The `ArduinoEthernet_GenerateEventExample` sketch is, predictably, for use with an Arduino Ethernet board or an Arduino with an Ethernet shield.  The `Hera200_GenerateEventExample` is for the custom Hera 200 hardware board developed by EyeHub partner Eseye.  The hackathon repository also holds the [Hera 200 schematic](Hera 200 schematic.pdf)

Both of these sketches use the [HttpClient](https://github.com/amcewen/HttpClient) library, which you'll need to install.  To do that you should copy the `HttpClient` folder into a `libraries` folder in your Arduino Sketchbook folder.  If you're unsure of where that is located you can find out by looking in the File -> Preferences menu in the Arduino IDE.  Once you have copied it across you will need to restart the Arduino IDE so that it finds the new library.
