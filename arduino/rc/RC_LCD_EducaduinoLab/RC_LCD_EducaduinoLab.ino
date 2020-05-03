/*
 *  Mesure de constante de temps d un circuit RC
 */

#include <LiquidCrystal.h>

#define pinE A11
#define pinC A9
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // Brochage de l'afficheur



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
    N=analogRead(pinC);
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
