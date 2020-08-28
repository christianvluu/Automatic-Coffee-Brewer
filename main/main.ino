#include <ArduinoJson.h>


#include <ArduinoJson.h>

boolean serialAvailable = false;
int internalTempSensor = A0; // this is incorrect, should just use MAX6675 sensor instead
int externalTempSensor = A1; // this is incorrect, should just use MAX6675 sensor instead
int heatRelay = 4;
int extractionPumpRelay = 5;
int coolingPumpRelay = 6;

boolean isHeating = false;
boolean isExtractionPumping = false;
boolean isCoolingPumping = false;

boolean trueFalseTrigger(char input) {
  char trueVal = "true";
  char falseVal = "false";
  if (input == falseVal) {
    return false;
  }
  else if (input == trueVal) {
    return true;
  }
  else {
    //Serial.print("ERROR in reading trueFalseTrigger");
  }
}

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
    else {

      // CHECK IF in_doc DICTIONARY HAS UPDATED COMMANDS IN IT
      isHeating = trueFalseTrigger(in_doc["heaterCommand"]);
      isExtractionPumping = trueFalseTrigger(in_doc["extractionPumpCommand"]);
      isCoolingPumping = trueFalseTrigger(in_doc["coolingPumpCommand"]);
  
  
      // send out_doc dictionary to Pi
      out_doc["heatStatus"] = isHeating;
      out_doc["extractionPumpStatus"] = isExtractionPumping;
      out_doc["coolingPumpStatus"] = isCoolingPumping;
      out_doc["internalTemp"] = -1;
      out_doc["externalTemp"] = -1;
    
      String out_payload;
      serializeJson(out_doc, out_payload);
  
      Serial.println(out_payload);
    }
  }
  else {
      serialAvailable = false;
      Serial.println("No Serial Available");
  }
}
