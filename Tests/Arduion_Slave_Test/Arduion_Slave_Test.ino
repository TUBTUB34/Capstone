#include <Wire.h>
#include <Adafruit_NeoPixel.h>

#define SLAVE_ADDRESS 0x09  // Unique I2C address for this Arduino

Adafruit_NeoPixel pixels(1, PIN_NEOPIXEL);

char currentColor = 'O';  // Store the current color

void setup() {
  Wire.begin(SLAVE_ADDRESS);  // Initialize the I2C bus with the given address
  Wire.onRequest(requestEvent);  // Register function to handle requests
  Wire.onReceive(receiveEvent);  // Register function to handle received data
  pixels.begin();  // Initialize the pixel
  
}

void loop() {
  delay(100);  // Main loop is empty; rely on interrupts
}

// Function to handle requests from the master (Raspberry Pi)
void requestEvent() {
  // Send the current color back to the master
  Wire.write(currentColor);
}

// Function to handle incoming data from the master (Raspberry Pi)
void receiveEvent(int howMany) {
  if (howMany >= 2) {  // Expecting at least two bytes
    char firstByte = Wire.read();  // Read the first byte
    char secondByte = Wire.read();  // Read the second byte
    Serial.println(secondByte);
    if (secondByte != '\0') {
      currentColor = secondByte;
      setColor(currentColor);
    }
  }
}

void setColor(char color) {
  if (color == 'R') {
    pixels.setPixelColor(0, pixels.Color(255, 0, 0));  // Red
  } else if (color == 'G') {
    pixels.setPixelColor(0, pixels.Color(0, 255, 0));  // Green
  } else if (color == 'B') {
    pixels.setPixelColor(0, pixels.Color(0, 0, 255));  // Blue
  } else {
    pixels.clear();  // Turn off the pixel
  }
  pixels.show();
}
