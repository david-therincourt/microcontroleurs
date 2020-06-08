from machine import I2C

i2c = I2C(scl="SCL", sda="SDA") # Port I2C
print(i2c.scan())