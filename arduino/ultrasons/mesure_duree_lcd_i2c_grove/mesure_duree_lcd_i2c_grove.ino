/*
 * Pilotage du module ultrason avec mesure de durée
 */

#include <Wire.h>       // Importation librairie gestion port I2C
#include "rgb_lcd.h"    // Importation librairie gestion afficheur LCD I2C Grove

#define pinTrig 8       // Trig sur broche 8
#define pinEcho 9       // Echo sur broche 9

long dureeEcho;         // Durée de l'Echo
rgb_lcd lcd;            // Déclaration de l'afficheur


void setup() {
  pinMode(pinTrig,OUTPUT);      // Broche Trig en sortie
  digitalWrite(pinEcho,LOW);    // Sortie Trig à l état bas
  pinMode(pinEcho,INPUT);       // Broche Echo en entrée
  lcd.begin(16,2);           // Paramétrage du port série
}

void loop() {
  digitalWrite(pinTrig,HIGH);            // Début impulsion de declenchement
  delayMicroseconds(10);                 // Attendre 10 microseconde
  digitalWrite(pinTrig,LOW);             // Fin impulsion (Etat bas)
  dureeEcho = pulseIn(pinEcho,HIGH);     // Mesure de la durée de l'impulsion sur Echo
  lcd.setCursor(0, 0); 
  lcd.print(dureeEcho);
  lcd.setCursor(8, 0); 
  lcd.print(" us");
  delay(1000);                           // Attendre 1s
}
