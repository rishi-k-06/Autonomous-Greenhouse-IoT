#include "WiFiEsp.h"
#include "SoftwareSerial.h"
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

SoftwareSerial Serial1(2, 3); // RX, TX for ESP-01
int moisturePin = A0;
int pumpRelay = 8;

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  dht.begin();
  pinMode(pumpRelay, OUTPUT);
  // WiFi initialization using WiFiEsp library
}

void loop() {
  float h = dht.readHumidity();
  int mRaw = analogRead(moisturePin);
  int mPercent = map(mRaw, 1023, 200, 0, 100);

  if (mPercent < 40) {
    digitalWrite(pumpRelay, HIGH); // Pump ON
  } else {
    digitalWrite(pumpRelay, LOW);  // Pump OFF
  }

  // Send data to Python via ESP-01 (Simplified Serial logic)
  Serial.print("M:"); Serial.print(mPercent);
  Serial.print(",H:"); Serial.println(h);
  
  delay(5000);
}
