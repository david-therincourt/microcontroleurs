/*
 * Mesure de la célérité du son au format CSV
 * avec un microntrôleur EducaduinoLab
 */

#define pinTrig 19      // Module ultrason sur
#define pinEcho 18      // les broches D18/D19

float distance = 1.735; // Distance en module et réflecteur
long  dureeEcho;        // Durée mesurée
float celerite;          // celerite obtenue
int n=1;                // Initialisation du compteur

void setup() {
  pinMode(pinTrig,OUTPUT);      // Broche Trig en sortie
  digitalWrite(pinEcho,LOW);    // Sortie Trig à l état bas
  pinMode(pinEcho,INPUT);       // Broche Echo en entrée
  Serial.begin(9600);           // Paramétrage du port série
  Serial.println("n;duree;v");  // Ecriture première ligne du CSV
}

void loop() {
  if (n<=100) {
  digitalWrite(pinTrig,HIGH);            // Déclenchement d une mesure : début impulsion (Etat haut)
  delayMicroseconds(10);                 // Attendre 10 microseconde
  digitalWrite(pinTrig,LOW);             // Fin impulsion (Etat bas)
  dureeEcho = pulseIn(pinEcho,HIGH);     // Mesure de la durée de l impulsion sur Echo
  celerite = 2*distance/dureeEcho*1E6;   // Calcul de la célérité
  Serial.print(n);                       // Début écriture ligne CSV
  Serial.print(";");
  Serial.print(dureeEcho);
  Serial.print(";");
  Serial.println(celerite);              // Fin écriture ligne CSV
  delay(100);                            // Attendre 100 ms
  n++;                                   // Incrémentation du compteur
  }
}
