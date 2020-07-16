from machine import I2C
from sm9541 import SM9541

i2c = I2C(freq=400000,sda=21,scl=22)
capt = SM9541(i2c,-40,40)

pressure = capt.read()
print(pressure)

i2c.deinit()