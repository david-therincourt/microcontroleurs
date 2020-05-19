from machine import I2C
from grove_i2c_adc import GroveADC

i2c = I2C(freq=400000, sda=21, scl=22)  # freq : 100kHz ou 400 kHz

can = GroveADC(i2c)
can.VREF = 3.085
N = can.read_voltage()
print(N)

i2c.deinit()
