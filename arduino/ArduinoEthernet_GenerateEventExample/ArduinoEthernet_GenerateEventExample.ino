// Simple example to retrieve a list of events for the Device
// given in DEVICE_ID and output the returned content to the serial port

#include <SPI.h>
#include <HttpClient.h>
#include <Ethernet.h>
#include <EthernetClient.h>

// You'll need to replace these with the details of your Device and user account
#define EYEHUB_DEVICE_MANAGER_ID  "YOUR DEVICE MANAGER ID"
#define EYEHUB_DEVICE_ID  "YOUR DEVICE ID"
#define EYEHUB_USERNAME  "YOUR EYEHUB USERNAME"
#define EYEHUB_PASSWORD  "YOUR EYEHUB PASSWORD"

// Name of the server we want to connect to
const char kHostname[] = "config28.flexeye.com";
// Path to download (this is the bit after the hostname in the URL
// that you want to download
const char kPath[] = "/v1/iot_Default/dms/" EYEHUB_DEVICE_MANAGER_ID "/devices/" EYEHUB_DEVICE_ID "/events";

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// Number of milliseconds to wait without receiving any data before we give up
const int kNetworkTimeout = 30*1000;
// Number of milliseconds to wait if no data is available before trying again
const int kNetworkDelay = 1000;

void setup()
{
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
  delay(500);
  Serial.println("Let's go!");

  while (Ethernet.begin(mac) != 1)
  {
    Serial.println("Error getting IP address via DHCP, trying again...");
    delay(15000);
  }  
}

void loop()
{
  int err =0;
  
  EthernetClient c;
  HttpClient http(c);

  http.beginRequest();  
  err = http.post(kHostname, kPath);
  if (err == 0)
  {
    Serial.println("startedRequest ok");
    // Send our login credentials
    //http.sendBasicAuth(EYEHUB_USERNAME, EYEHUB_PASSWORD);
    http.sendHeader("Authorization: Basic YWRyaWFubUBtY3FuLmNvbTphZHJpYW5tQG1jcW4uY29t");
    
    // Tell the server that we'll be sending some JSON data over
    http.sendHeader("Content-Type", "application/json");
    
    // Work out how much data we're going to send
    // THIS NEEDS TO EXACTLY MATCH THE STUFF WE SEND LATER ON
    int content_len = 0;
    content_len += strlen("{ ");
    content_len += strlen("\"type\":\"1.0\", ");
    content_len += strlen("\"source\":\"test_sensor\", ");
    content_len += strlen("\"payload\":\"56\"");
    content_len += strlen("}");
    // And tell the server
    http.sendHeader("Content-Length", content_len);
    
    // Now send the data over
    // THIS NEEDS TO EXACTLY MATCH THE STUFF WE CALCULATED THE LENGTH OF ABOVE
    http.print("{ ");
    http.print("\"type\":\"1.0\", ");
    http.print("\"source\":\"test_sensor\", ");
    http.print("\"payload\":\"56\"");
    http.print("}");

    http.endRequest();

    err = http.responseStatusCode();
    if (err >= 0)
    {
      Serial.print("Got status code: ");
      Serial.println(err);

      // Usually you'd check that the response code is 200 or a
      // similar "success" code (200-299) before carrying on,
      // but we'll print out whatever response we get

      err = http.skipResponseHeaders();
      if (err >= 0)
      {
        int bodyLen = http.contentLength();
        Serial.print("Content length is: ");
        Serial.println(bodyLen);
        Serial.println();
        Serial.println("Body returned follows:");
      
        // Now we've got to the body, so we can print it out
        unsigned long timeoutStart = millis();
        char c;
        // Whilst we haven't timed out & haven't reached the end of the body
        while ( (http.connected() || http.available()) &&
               ((millis() - timeoutStart) < kNetworkTimeout) )
        {
            if (http.available())
            {
                c = http.read();
                // Print out this character
                Serial.print(c);
               
                bodyLen--;
                // We read something, reset the timeout counter
                timeoutStart = millis();
            }
            else
            {
                // We haven't got any data, so let's pause to allow some to
                // arrive
                delay(kNetworkDelay);
            }
        }
      }
      else
      {
        Serial.print("Failed to skip response headers: ");
        Serial.println(err);
      }
    }
    else
    {    
      Serial.print("Getting response failed: ");
      Serial.println(err);
    }
  }
  else
  {
    Serial.print("Connect failed: ");
    Serial.println(err);
  }
  http.stop();

  // And just stop, now that we've tried a download
  char l = ' ';
  while(l != '\n')
  {
    if (Serial.available() > 0)
    {
      l = Serial.read();
    }
  }
  Serial.println("\n\n===================================\nLooping round for another go!\n");
}


