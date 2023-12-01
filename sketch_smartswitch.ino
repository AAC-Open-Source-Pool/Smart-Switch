#include <Arduino.h>
#include <WiFi.h>
#include <FirebaseESP32.h>

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

// Insert your network credentials
#define WIFI_SSID "walter"
#define WIFI_PASSWORD "gustavowhite"

// Insert Firebase project API Key
#define API_KEY "AIzaSyAz9thDEv7--mATBZYy5KrM-OTriNwEeIQ"


// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://smart-switch-bc1db-default-rtdb.asia-southeast1.firebasedatabase.app/" 
int led1 = 4;
int led2 = 5;

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
int count = 0;
bool signupOK = false;
String str1="****";
String str2 = "#####";

void setup(){
  Serial.begin(115200);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  digitalWrite(led1,HIGH);
  digitalWrite(led2,HIGH);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(200);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);



}

void loop(){
  if (Firebase.ready() && signupOK && (millis() - sendDataPrevMillis > 300 || sendDataPrevMillis == 0)){
    sendDataPrevMillis = millis();
    // Write an Int number on the database path test/int
  String firebasePath = "Users/Led1";
  if (Firebase.getString(fbdo, firebasePath)) {
    if (fbdo.stringData().length() > 0) {
      Serial.print("Value at ");
      Serial.print(firebasePath);
      Serial.print(": ");
      str1 = fbdo.stringData();
    }
  } else {
    Serial.print("Failed to read from Firebase: ");
    Serial.println(fbdo.errorReason());
  }

  firebasePath = "Users/Led2";
  if (Firebase.getString(fbdo, firebasePath)) {
    if (fbdo.stringData().length() > 0) {
      Serial.print("Value at ");
      Serial.print(firebasePath);
      Serial.print(": ");
      str2 = fbdo.stringData();
    }
  } 
  else {
    Serial.print("Failed to read from Firebase: ");
    Serial.println(fbdo.errorReason());
  }


    Serial.print("Led1: ");
    Serial.print(str1);
    Serial.print(" ");
    Serial.print("Led2: ");
    Serial.println(str2);
  }

  //turning led1 on/off
  if(str1=="on")
  {
    digitalWrite(led1,LOW);
    
  }
  else
  {
    digitalWrite(led1,HIGH);
  }


  //turning led2 on/off
    if(str2=="on")
  {
    digitalWrite(led2,LOW);
  }
  else
  {
    digitalWrite(led2,HIGH);
  }



  delay(200);
}