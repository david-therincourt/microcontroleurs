/*
 * Pilotage du module ultrason avec mesure de durée
 */

#define pinTrig 8       // Trig sur broche 8
#define pinEcho 9       // Echo sur broche 9

long dureeEcho;         // Durée de l'Echo

void setup() {
  pinMode(pinTrig,OUTPUT);      // Broche Trig en sortie
  digitalWrite(pinEcho,LOW);    // Sortie Trig à l état bas
  pinMode(pinEcho,INPUT);       // Broche Echo en entrée
  Serial.begin(9600);           // Paramétrage du port série
}

void loop() {
  digitalWrite(pinTrig,HIGH);            // Début impulsion de declenchement
  delayMicroseconds(10);                 // Attendre 10 microseconde
  digitalWrite(pinTrig,LOW);             // Fin impulsion (Etat bas)
  dureeEcho = pulseIn(pinEcho,HIGH);     // Mesure de la durée de l'impulsion sur Echo
  Serial.print("Durée (µs) = ");          // Affichage sur port série
  Serial.println(dureeEcho);
  delay(1000);                           // Attendre 1s
}
