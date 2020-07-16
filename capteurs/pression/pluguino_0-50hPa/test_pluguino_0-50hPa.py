# Capteur Pluginguino pression manomètre 0-50 hPA / 0.5-4.5V

from machine import I2C
from ads1x15 import ADS1115
from time import sleep_ms

i2c = I2C(1)
adc = ADS1115(i2c,0x48,0) # 0 : 6.144V # 2/3x 
Vref = 6.100              # 6.144 V ajust to 6.10
Nmax = 32765              # 2^15 - 1

U = adc.read()*Vref/Nmax  
P = 5000/4*(U-0.5)
print(U, P)
sleep_ms(1000)
