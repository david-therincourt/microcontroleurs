/*
 *  Mesure de constante de temps d un circuit RC
 */

#include <Wire.h>       // Importation librairie gestion port I2C
#include "rgb_lcd.h"    // Importation librairie gestion afficheur LCD I2C Grove

#define pinE A1

float R = 100;    // Resistance kOhm
int N = 0;
unsigned long t0;
unsigned long t1;
unsigned long tau;
float C;

rgb_lcd lcd;            // Déclaration de l'afficheur

void setup() {
  lcd.begin(16, 2);                      // Fixe 2 colonnes et 16 caractères/ligne
  lcd.setRGB(125, 125, 125);    // Fixe couleur de fond
  pinMode(pinE,OUTPUT);
  digitalWrite(pinE,LOW);
  delay(1000);
  digitalWrite(pinE,HIGH);
  t0 = micros();
  while (N<646) {      // Seuil = 0,632*1023 = 646
    N=analogRead(A0);
  }
  t1 = micros();
  digitalWrite(pinE,LOW);
  tau = t1 - t0;
  C = tau/R;
  lcd.setCursor(0, 0); 
  lcd.print(tau);
  lcd.setCursor(8, 0); 
  lcd.print(" us");
  lcd.setCursor(0, 1); 
  lcd.print(C);
  lcd.setCursor(8, 1); 
  lcd.print(" nF");
  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:
}
