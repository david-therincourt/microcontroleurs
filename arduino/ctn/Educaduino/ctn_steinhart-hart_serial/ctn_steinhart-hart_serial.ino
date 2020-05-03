/*
 * Mesure de la température avec la relation de Steinhart-Hart
 */

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
   Serial.begin(9600);  // Paramétrage du port série
}

void loop() {
   u = analogRead(A9)*5.0/1023;                  // Lecture tension en V
   R = Ro * u/(Vcc-u);                           // Calcul de la résistance
   logR = log(R);                                // Calcul de ln(R)
   T = (1.0 / (A + B*logR + C*logR*logR*logR));  // Calcul de la température
   T = T - 273.15;                               // Conversion en °C
   Serial.print("R = ");                         // Début affichage
   Serial.println(R);
   Serial.print("T = ");
   Serial.println(T);                            // Fin affichage
   delay(1000);                                  // Temporisation de 1s
}
