// #include <ArduinoJson.h>


// #include <ArduinoJson.h>

// boolean serialAvailable = false;
// int internalTempSensor = A0; // this is incorrect, should just use MAX6675 sensor instead
// int externalTempSensor = A1; // this is incorrect, should just use MAX6675 sensor instead
// int heatRelay = 4;
// int extractionPumpRelay = 5;
// int coolingPumpRelay = 6;

// boolean isHeating = false;
// boolean isExtractionPumping = false;
// boolean isCoolingPumping = false;

// // boolean trueFalseParser(string input) {
// //   string trueVal = "true";
// //   string falseVal = "false";
// //   if (input == falseVal) {
// //     return false;
// //   }
// //   else if (input == trueVal) {
// //     return true;
// //   }
// //   else {
// //     //Serial.print("ERROR in reading trueFalseTrigger");
// //   }
// // }

// // string trueFalseEncoder(boolean input) {
// //   string trueVal = "true";
// //   string falseVal = "false";
// //   if (input == false) {
// //     return falseVal;
// //   }
// //   else if (input == true) {
// //     return trueVal;
// //   }
// //   else {
// //     //
// //   }
// // }

// void setup() {
//   Serial.begin(9600);
//   pinMode(internalTempSensor, INPUT);
//   pinMode(externalTempSensor, INPUT);
//   pinMode(heatRelay, OUTPUT);
//   pinMode(extractionPumpRelay, OUTPUT);
//   pinMode(coolingPumpRelay, OUTPUT);
// }

// void loop() {

//   if (Serial.available() > 0) {
//     serialAvailable = true;
//     StaticJsonDocument<512> in_doc; // input document
//     StaticJsonDocument<512> out_doc; // declare new ones for Json Documents, do not change values because of memory leak

//     String in_payload = Serial.readStringUntil('\n');
    
//     DeserializationError error = deserializeJson(in_doc, in_payload);
    
//     if (error) {
//       Serial.println("ERROR");
//     }
//     else {

//       // CHECK IF in_doc DICTIONARY HAS UPDATED COMMANDS IN IT
//       isHeating = false;
//       isExtractionPumping = false;
//       isCoolingPumping = false;
  
  
//       // send out_doc dictionary to Pi
//       out_doc["heatStatus"] = false;
//       out_doc["extractionPumpStatus"] = false;
//       out_doc["coolingPumpStatus"] = false;
//       out_doc["internalTemp"] = "-1";
//       out_doc["externalTemp"] = "-1";
    
//       String out_payload;
//       serializeJson(out_doc, out_payload);
  
//       Serial.println(out_payload);
//     }
//   }
//   else {
//       serialAvailable = false;
//       Serial.println("No Serial Available");
//   }
// }


#include <ArduinoJson.h>

int internalTempSensor = A0; // this is incorrect, should just use MAX6675 sensor instead
int externalTempSensor = A1; // this is incorrect, should just use MAX6675 sensor instead
int heatRelay = 4;
int extractionPumpRelay = 5;
int coolingPumpRelay = 6;
long lastSerialCommTime;

void setup() {
  Serial.begin(9600);
  Serial.begin(9600);
  pinMode(internalTempSensor, INPUT);
  pinMode(externalTempSensor, INPUT);
  pinMode(heatRelay, OUTPUT);
  pinMode(extractionPumpRelay, OUTPUT);
  pinMode(coolingPumpRelay, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    lastSerialCommTime = millis();
    StaticJsonDocument<512> in_doc;
    StaticJsonDocument<512> out_doc; // declare new ones for Json Documents, do not change values because of memory leak

    String in_payload = Serial.readStringUntil('\n');
    
    DeserializationError error = deserializeJson(in_doc, in_payload);
    
    if (error) {
      Serial.println("ERROR");
    }

    digitalWrite(heatRelay, in_doc["nowHeat"]);


    out_doc["heatState"] = in_doc["nowHeat"];
    out_doc["extractState"] = in_doc["nowExtract"];
    out_doc["coolState"] = in_doc["nowCool"];
    String out_payload;
    serializeJson(out_doc, out_payload);

    Serial.println(out_payload);
  }
  else {
    if (lastSerialCommTime + 3000 < millis()) {
      digitalWrite(heatRelay, LOW);
      digitalWrite(extractionPumpRelay, LOW);
      digitalWrite(coolingPumpRelay, LOW);
    }
  }
}