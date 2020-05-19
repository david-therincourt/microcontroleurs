# M5Stack ESP32
# Mesure de température à l'aide d'une CTN 10k
# dans un pont diviseur de tension Ro = 10 kOhm
# CAN 16 bits I2C AS1115 

from machine import I2C
from ads1x15 import ADS1115

i2c = I2C(freq=400000,sda=21,scl=22)
adc = ADS1115(i2c,0x48,0) # Gain value - 0 : 6.144V # 2/3x


R0 = 10E3      # 10k ohm
Nmax = 26860   # 5/6.144*32765 = 26664
N = adc.read()
R =  R0*(Nmax/N - 1)
print(R)

    
i2c.deinit() # Close I2C