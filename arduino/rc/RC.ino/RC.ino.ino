/*
 *  Mesure de constante de temps d un circuit RC
 */

#define pinE 8

int N = 0;
int Nmax = 372;
int Nseuil = 233;
unsigned long t0;
unsigned long t1;
unsigned long Dt;
float R = 1E6; 
float C;



void setup() {
  Serial.begin(9600);
  Serial.println("Start");
  pinMode(pinE,OUTPUT);      // Broche digitale en sortie     

  digitalWrite(pinE,LOW);    // Décharge condensateur avant mesure
  delay(1000);               // pendant 1s

  digitalWrite(pinE,HIGH);   // Début charge condensateur
  t0 = micros();             // Mesure instant initial
  while (N<Nseuil) {            // Boucle tant que tension inférieure à seuil (0,632*1023=646)
    N=analogRead(A0);        // Lecture tension condensateur
  }
  t1 = micros();             // Mesure instant où seuil atteint
  Dt = t1 - t0;              // Calcul de tau
  C = Dt*1E6/R;             // Calcul de C connaissant R
  Serial.print(Dt);          // Début affichage
  Serial.println(" µs");
  Serial.print(C);
  Serial.println(" nF");     // Fin affichage
  digitalWrite(pinE,LOW);    // Début décharge condensateur
  delay(1000);
  N=analogRead(A0);        // Lecture tension condensateur
  Serial.print(N);          // Début affichage
}

void loop() {
  // put your main code here, to run repeatedly:
}
