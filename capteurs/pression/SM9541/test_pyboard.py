from machine import I2C
from sm9541 import SM9541
from time import sleep_ms

i2c = I2C(1)
capt = SM9541(i2c,-40,40)

while True:
    pressure = capt.read()
    print(pressure)
    sleep_ms(1000)
