// demo of Starter Kit V2.0 - Grove Temperature Sensor
//




// Caractérisitque CTN
int beta=3280;         // Beta value of the thermistor 3435
float To=292;          // Temperature en Kelvin 298,15 K (25°C)
float Ro=12620;        // Résistance reference 10k
int R1=10000;

int N;
float temperature;
float resistance;
float temps;

void setup()
{
    Serial.begin(9600);     //Baud rate for the serial communication of Arduino
    Serial.println("temps,T");
}

void loop()
{
    temps=millis()/1000;
    int N = analogRead(A0);                               // get analog value
    resistance=(float)N/(1023-N)*R1;                      // get resistance
    temperature=1/(log(resistance/Ro)/beta+1/To)-273.15;     // calc temperature
    Serial.print(temps);
    Serial.print(",");
    Serial.println(temperature);    
    delay(1000);          // delay 1s
}
