// Mesure de la résistance d'une CTN et calcul de la température

// Caractéristique CTN
#define  beta 3280      // Beta value of the thermistor 3435
#define  To   292       // Temperature en Kelvin 298,15 K (25°C)
#define  Ro   12620     // Résistance reference 10k
#define  R1   10000     // Résistance du pont diviseur de tension

int N;
float R;           // Résistance
float T;           // Température

void setup()
{
    Serial.begin(9600);     //Baud rate for the serial communication of Arduino
}

void loop()
{
    N = analogRead(A0);                         // Mesure de la tension
    R = (float) R1*N/(1023-N);                  // Calcul de la résistance
    T = log(R/Ro)/beta + (float)1/To;           // Calcul de la température
    T = 1/T-273.15;                             // Suite calcul
    Serial.println(R);                          // Affichage de la résistance
    Serial.println(T);                          // Affichage de la température
    delay(1000);
}
