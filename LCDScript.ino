// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
// LCD dimentions
const int xlen = 16, ylen = 2;

int incomingByte = 0; // for incoming serial data
String incomingString = "";

// make some custom characters:
byte heart[8] = {
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000
};

byte smiley[8] = {
  0b00000,
  0b00000,
  0b01010,
  0b00000,
  0b00000,
  0b10001,
  0b01110,
  0b00000
};

byte frownie[8] = {
  0b00000,
  0b00000,
  0b01010,
  0b00000,
  0b00000,
  0b00000,
  0b01110,
  0b10001
};

byte armsDown[8] = {
  0b00100,
  0b01010,
  0b00100,
  0b00100,
  0b01110,
  0b10101,
  0b00100,
  0b01010
};

byte armsUp[8] = {
  0b00100,
  0b01010,
  0b00100,
  0b10101,
  0b01110,
  0b00100,
  0b00100,
  0b01010
};

// default message
void def_message(){
  //print the character
  lcd.setCursor(0,0);
  lcd.write(byte(0));
  // Print a message to the LCD.
  lcd.setCursor(1,0);
  lcd.print("Viewers count");
  //print the character
  lcd.setCursor(14,0);
  lcd.write(byte(0));
}

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(xlen, ylen);
  // Opens the serial port, sets data rate to 9600 bps
  Serial.begin(115200);
  Serial.setTimeout(1);

  //print the default message
  def_message();

  // create a new character
  lcd.createChar(0, heart);
  // create a new character
  lcd.createChar(1, smiley);
  // create a new character
  lcd.createChar(2, frownie);
  // create a new character
  lcd.createChar(3, armsDown);
  // create a new character
  lcd.createChar(4, armsUp);
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    //clear the schreen
    lcd.clear();
    //print the default message
    def_message();
    // Read the String from the Serial port
    incomingString = Serial.readString();

    // center the folowing text
    int center = xlen / 2 - incomingString.length() / 2 - 1;
    // set the cursor to column 0, line 1
    lcd.setCursor(center,1);
    //print the data getted into the LCD
    
    lcd.print(incomingString);
  }
}
