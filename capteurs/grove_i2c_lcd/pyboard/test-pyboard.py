# Afficheur Grove I2C LCD v1.0
# Test sur les cartes :
#  - Pyboard
#  - Feather STM32F405 Express
#  - Nucleo 64 STM32F401RE

from machine import I2C
from grove_lcd import Lcd

i2c = I2C(1)         # Premier port I2C
lcd = Lcd(i2c,16,2)

lcd.clear()
lcd.print("Hello")
lcd.setCursor(0,1)
lcd.print("Pyboard")
