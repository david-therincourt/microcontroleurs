/*
 * Mesure d'un température avec une CTN 10k (25°C)
 * placée dans un pont diviseur de tension avec
 * une résistance de 10k.
 */

float tension;
int temperature;    // Arrondi à l'entier
float a = -0.0441;  // Coeff. directeur modèle
float b = 3.66;     // Ordonnée à l'origine modèle

void setup() {
  Serial.begin(9600);  // Paramétrage du port série

}

void loop() {
  tension = analogRead(A0)*5.0/1023; // Lecture tension
  temperature = (tension-b)/a;       // Calcul température
  Serial.print("U = ");              // Affichage dans moniteur série
  Serial.println(tension);
  Serial.print("T= ");
  Serial.println(temperature);
  delay(1000);                       // Temporisation
}
