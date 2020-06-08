from machine import I2C
from honeywell_hsc import HSC
from time import sleep_ms

i2c = I2C(scl="SCL", sda="SDA")

hsc = HSC(i2c, p_min=0, p_max=2068) # 30 PSI = 2068 hPa

for i in range(10):
    pressure = hsc.read()
    print(pressure)
    sleep_ms(100)
