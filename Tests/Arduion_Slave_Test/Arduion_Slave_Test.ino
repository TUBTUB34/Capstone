#include <Wire.h>

#define SLAVE_ADDRESS 0x0a  // Unique I2C address for this Arduino


int voltage = 12;  //test voltage
int current = 2;   //test current
int power = voltage*current;
char command;

void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);  // Initialize the I2C bus with the given address
  Wire.onRequest(requestEvent);  // Register function to handle requests
  Wire.onReceive(receiveEvent);  // Register function to handle received data
  
}

void loop() {
  delay(100);  // Main loop is empty; rely on interrupts
}


void requestEvent() {
  // Send  back to the master
  if (command == 'V'){
    Wire.write(voltage);
  }
  else if (command == 'C') {
    Wire.write(current);
  }4
  else if (command == 'P') {
    Wire.write(power);
  }
  
}

// Function to handle incoming data from the master (Raspberry Pi)
void receiveEvent(int howMany) {
    char garbage = Wire.read();  // Read the first byte
    command = Wire.read();  // Read the second byte
    Serial.println(command);

}

/*
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
*/
