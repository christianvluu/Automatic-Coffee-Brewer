
#include <ArduinoJson.h>

boolean serialAvailable = false;
int internalTempSensor = A0; // this is incorrect, should just use MAX6675 sensor instead
int externalTempSensor = A1; // this is incorrect, should just use MAX6675 sensor instead
int heatRelay = 4;
int extractionPumpRelay = 5;
int coolingPumpRelay = 6;

int 

void setup() {
  Serial.begin(9600);
  pinMode(internalTempSensor, INPUT);
  pinMode(externalTempSensor, INPUT);
  pinMode(heatRelay, OUTPUT);
  pinMode(extractionPumpRelay, OUTPUT);
  pinMode(coolingPumpRelay, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    serialAvailable = true;
    StaticJsonDocument<512> in_doc; // input document
    StaticJsonDocument<512> out_doc; // declare new ones for Json Documents, do not change values because of memory leak

    String in_payload = Serial.readStringUntil('\n');
    
    DeserializationError error = deserializeJson(in_doc, in_payload);
    
    if (error) {
      Serial.println("ERROR");
    }

    // CHECK IF in_doc DICTIONARY HAS UPDATED COMMANDS IN IT


    // send out_doc dictionary to Pi
    out_doc["1"] = "send from Arduino part 1";
    out_doc["2"] = "send from arduino part 2";
    String out_payload;
    serializeJson(out_doc, out_payload);

    Serial.println(out_payload);
  }
  else {
      serialAvailable = false
  }
}