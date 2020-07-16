# Test DFRobot Gravity I2C ADC 16 bits ADS1115

from machine import I2C
from ads1x15 import ADS1115
from time import sleep_ms

i2c = I2C(1)

adc = ADS1115(i2c,0x48,0)

# adc = ADS1115(i2c, address, gain)
# Gain value - 0 as default
# 0 : 6.144V # 2/3x
# 1 : 4.096V # 1x
# 2 : 2.048V # 2x
# 3 : 1.024V # 4x
# 4 : 0.512V # 8x
# 5 : 0.256V # 16x


N = adc.read()
U = N*6.144/32765
print(N, U)
sleep_ms(1000)
