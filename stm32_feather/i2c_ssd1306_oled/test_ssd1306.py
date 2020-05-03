# Voir class FrameBuffer pour les méthodes d'écriture et de dessin

from pyb import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl = Pin('SCL'), sda = Pin('SDA'))
oled = SSD1306_I2C(128, 32, i2c, 0x3c)
oled.fill(0)
oled.text("Hello David", 0, 0)
oled.text("R =", 0, 10)
oled.show()