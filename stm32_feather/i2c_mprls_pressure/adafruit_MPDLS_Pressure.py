# Absolute pressure MPRLS 0-25 psi I2C
# David THERINCOURT

from pyb import Pin
from machine import I2C
from struct import unpack
from time import sleep_ms

adr = 24
_psimin = 0
_psimax = 25


i2c = I2C(scl = Pin('SCL'), sda = Pin('SDA'))

buffer = b'\xAA\x00\x00'  # 0xAA followed by 0x00 and 0x00 to exit Stanby Mode 
i2c.writeto(adr, buffer)  # write buffer

sleep_ms(200)

data = bytearray(4)   # 32 bit = Status + Data(23:16) + Data(15:8) + Data(7:0)
i2c.readfrom_into(adr, data)  # Read data
print(data)
    
raw_psi = (data[1] << 16) | (data[2] << 8) | data[3]
psi = (raw_psi - 0x19999A) * (_psimax - _psimin)
psi /= 0xE66666 - 0x19999A
psi += _psimin
p = psi * 68.947572932   # hPa

print(psi)
print(p)


