/*
 * Mesure de la température avec la relation de Steinhart-Hart
 */

#include <LiquidCrystal.h>        // Importation de la librairie LiquidCrystal

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // Brochage de l'afficheur

#define Vcc 5       // Tension d'alimentation
#define Ro  10000   // Résistance du pont
#define A   1.0832e-3
#define B   2.1723e-4
#define C   3.2770e-7

float u;            // Tension CTN
float R;            // Résistance CTN
float logR;         // ln(R)
float T;            // Température en °C


void setup() {
   lcd.begin(16, 2);     // fixe le nombre de colonnes et de lignes de l afficheursérie
   lcd.setCursor(0,0);   // place le curseur à la colonne 5 et à la ligne 0
   lcd.print("Temperature "); // Affiche un texte
   
}

void loop() {
   u = analogRead(A9)*5.0/1023;                  // Lecture tension en V
   R = Ro * u/(Vcc-u);                           // Calcul de la résistance
   logR = log(R);                                // Calcul de ln(R)
   T = (1.0 / (A + B*logR + C*logR*logR*logR));  // Calcul de la température
   T = T - 273.15;                               // Conversion en °C
   lcd.setCursor(0,1);                           // place le curseur à la colonne 0 et à la ligne 1
   lcd.print(T);                                 // Affiche un autre texte
   lcd.print((char)223);
   lcd.print("C");
   delay(1000);                                  // Temporisation de 1s
}
