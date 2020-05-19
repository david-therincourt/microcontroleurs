# M5Stack ESP32
# Mesure de température avec le capteur CTN PlugUino
# Ro = 10 kOhm reliée à la masse
# CAN 16 bits I2C AS1115

from machine import I2C
from ads1x15 import ADS1115
from time import sleep_ms
from math import log


i2c = I2C(freq=400000,sda=21,scl=22)
adc = ADS1115(i2c,0x48,0) # Gain value - 0 : 6.144V # 2/3x

# Coefficients de Steinhart-Hart
A = 1.0832e-3
B = 2.1723e-4
C = 3.2770e-7

Nmax = 26860   # 5/6.144*32765 = 26664
Ro = 10e3

def mesure_resistance_up():
    return  Ro*(Nmax/adc.read() - 1)

while not buttonA.wasPressed():
    R = mesure_resistance_up()
    print(R)
    logR = log(R)
    T = 1/(A + B*logR + C*logR**3) - 273.15  #
    print(T)
    sleep_ms(1000)

i2c.deinit() # Close I2C
