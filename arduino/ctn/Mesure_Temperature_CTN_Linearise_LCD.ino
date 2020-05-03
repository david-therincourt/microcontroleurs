/*
 * Mesure d'un température avec une CTN 10k (25°C)
 * placée dans un pont diviseur de tension avec
 * une résistance de 10k.
 */

#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

float tension;
float temperature;    // Arrondi à l'entier
float a = -0.0441;  // Coeff. directeur modèle
float b = 3.66;     // Ordonnée à l'origine modèle

void setup() {
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(5, 0);
  lcd.print("V");
  lcd.setCursor(7, 1);
  lcd.write(223);
  lcd.setCursor(8, 1);
  lcd.print("C");
}

void loop() {
  tension = analogRead(A0)*5.0/1023; // Lecture tension
  temperature = (tension-b)/a;       // Calcul température
  lcd.setCursor(0, 0);
  lcd.print(tension);
  lcd.setCursor(0, 1);
  lcd.print(temperature);
  
  delay(1000);                       // Temporisation
}
