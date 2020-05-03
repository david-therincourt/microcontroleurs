/*
 *  Mesure de constante de temps d un circuit RC
 */

#include <LiquidCrystal.h>

#define pinE 11
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);        // select the pins used on the LCD panel



int N = 0;
unsigned long t0;
unsigned long t1;
unsigned long Dt;
float C;


void setup() {
  lcd.begin(16, 2);                       // start the library
  pinMode(pinE,OUTPUT);
  digitalWrite(pinE,LOW);
  delay(1000);
  digitalWrite(pinE,HIGH);
  t0 = micros();
  while (N<646) {      // Seuil = 0,632*1023 = 646
    N=analogRead(A1);
  }
  t1 = micros();
  Dt = t1 - t0;
  C = Dt/1000.0;
  lcd.setCursor(0, 0); 
  lcd.print(Dt);
  lcd.setCursor(8, 0); 
  lcd.print(" us");
  lcd.setCursor(0, 1); 
  lcd.print(C);
  lcd.setCursor(8, 1); 
  lcd.print(" nF");
  //delay(1000);
  digitalWrite(pinE,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
}
