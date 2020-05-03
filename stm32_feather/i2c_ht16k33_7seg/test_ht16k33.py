# Copier ht16k33_matrix.py et ht16k33_seg dans /lib de la Pyboard
# Test sur STM32F405 Feather Express

from pyb import Pin
from machine import I2C
from ht16k33_seg import Seg7x4

i2c = I2C(scl = Pin('SCL'), sda = Pin('SDA'))
aff = Seg7x4(i2c, address = 0x70)

aff.text("47.5")
aff.show()
