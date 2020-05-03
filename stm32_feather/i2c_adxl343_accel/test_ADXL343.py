# Voir class FrameBuffer pour les méthodes d'écriture et de dessin

from pyb import Pin
from machine import I2C
from struct import unpack
from time import sleep_ms

_REG_POWER_CTL = const(0x2D)  # Power-saving features control
_REG_INT_ENABLE = const(0x2E)  # Interrupt enable control
_REG_DATA_FORMAT = const(0x31)  # Data format control
_REG_DATAX0 = const(0x32)  # X-axis data 0
_REG_DATAX1 = const(0x33)  # X-axis data 1
_REG_DATAY0 = const(0x34)  # Y-axis data 0
_REG_DATAY1 = const(0x35)  # Y-axis data 1
_REG_DATAZ0 = const(0x36)  # Z-axis data 0
_REG_DATAZ1 = const(0x37)  # Z-axis data 1

i2c = I2C(scl = Pin('SCL'), sda = Pin('SDA'))

i2c.writeto_mem(83, _REG_POWER_CTL, b'\x08')  # Active le bit "Mesure"
i2c.writeto_mem(83, _REG_INT_ENABLE, b'\x00')

def accel():
    reg = i2c.readfrom_mem(83, _REG_DATAX0, 6)
    x, y, z = unpack("<hhh", reg)
    gx = x * 0.004 * 9.80665
    gy = y * 0.004 * 9.80665
    gz = z * 0.004 * 9.80665
    return gx, gy, gz

N = 10
x = [0 for i in range(N)]
y = [0 for i in range(N)]
z = [0 for i in range(N)]

for i in range(10):
    x[i], y[i], z[i] = accel()
    sleep_ms(100)

data = (x, y, z)
print(data)
    
    



