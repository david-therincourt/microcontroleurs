from machine import I2C

i2c = I2C(1)
i2c.scan()