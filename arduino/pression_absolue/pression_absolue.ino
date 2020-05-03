/*
* Mesure d une pression absolue
* Capteur Educaduino 200 hPa à 4000 hPa
* branché sur la broche A9
*/

#define brocheCapteur A9      // Numéro de broche connectée au capteur
#include <LiquidCrystal.h>    // Librairie de gestion de l écran LCD

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // Déclaration de l écran LCD


float tension ;               // Tension mesurée
float pression ;              // Pression mesurée

void setup() {
lcd.begin(16, 2);           // Paramétrage de l ecran LCD

}

void loop() {
tension = analogRead(brocheCapteur)*5.0/1023 ;   // Lecture de la tension
pression = tension * 76 + 20 ;                 // Calcul de la pression en hPa
lcd.clear();                                     // Début affichage
lcd.setCursor(0,0);
lcd.print("Pression");
lcd.setCursor(0,1);
lcd.print(pression);
lcd.print(" kPa");                               // Fin affichage
delay(1000);
}
