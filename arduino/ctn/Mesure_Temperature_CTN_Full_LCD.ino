// demo of Starter Kit V2.0 - Grove Temperature Sensor
//

#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

// Caractérisitque CTN
int beta=3280;         // Beta value of the thermistor 3436 K
float To=292;          // Temperature en Kelvin 298,15 K (25°C)
float Ro=12620;        // Résistance reference 10k
int R1=10000;

int N;
float temperature;
float resistance;

void setup()
{
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(10, 0);
  lcd.write(244);        // Caractère spécial Oméga
  lcd.setCursor(7, 1);
  lcd.write(223);        // Caractère spécial °
  lcd.setCursor(8, 1);
  lcd.print("C");
}
    

void loop()
{
    int N = analogRead(A0);                               // get analog value
    resistance=(float)N/(1023-N)*R1;                      // get resistance
    temperature=1/(log(resistance/Ro)/beta+1/To)-273.15;     // calc temperature
    lcd.setCursor(0, 0);
    lcd.print(resistance);
    lcd.setCursor(0, 1);
    lcd.print(temperature);   
    delay(1000);          // delay 1s
}
