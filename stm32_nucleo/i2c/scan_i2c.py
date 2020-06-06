from machine import I2C

i2c = I2C(1)
print(i2c.scan())