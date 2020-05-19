# M5Stack ESP32
# Mesure de température à l'aide d'une CTN 10k
# dans un pont diviseur de tension Ro = 10 kOhm
# CAN 16 bits I2C AS1115 

from machine import I2C
from ads1x15 import ADS1115

import time
from math import log

from m5stack import lcd, buttonA



i2c = I2C(freq=400000,sda=21,scl=22)
adc = ADS1115(i2c,0x48,0)

# adc = ADS1115(i2c, address, gain)
# Gain value - 0 as default
# 0 : 6.144V # 2/3x
# 1 : 4.096V # 1x
# 2 : 2.048V # 2x
# 3 : 1.024V # 4x
# 4 : 0.512V # 8x
# 5 : 0.256V # 16x

lcd.font(lcd.FONT_DejaVu24)
lcd.clear()
lcd.text(lcd.CENTER, 0,'ADS1115 - CTN')
#lcd.text(lcd.CENTER,30,'I2C ADC 16 bits')
lcd.text(40,210,'Stop')

# Coefficients de Steinhart-Hart
A = 1.0832e-3
B = 2.1723e-4
C = 3.2770e-7
Vcc = 5.0
Ro = 10e3

while not buttonA.wasPressed():
    # Conversion analogique/numérique
    N = adc.read()
    print(N)
    lcd.text(20,60,'N= %d        ' %N)
    # Calcul de la tension
    U = N*6.105/32767  # 6.144V - valeur réelle 6.105 V sur 11 bits
    print(U)
    lcd.text(20,90,'U= %.3f V   ' %U)
    # Calcul de la resistance
    R = Ro*U/(Vcc-U)
    print(R)
    lcd.text(20,120,'R = %.0f Ohm   ' %R)
    # Calcul de la temperature
    logR = log(R)
    T = 1/(A + B*logR + C*logR**3) - 273.15  #
    print(T)
    lcd.text(20,150,'T = %.2f Celsius   ' %T)
    # Temporisation
    time.sleep_ms(1000)

lcd.text(lcd.CENTER,180,"** Fin **")
lcd.textClear(40,210,'Stop')
i2c.deinit() # Close I2C