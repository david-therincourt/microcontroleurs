# Le port I2C ne fonctionne pas !!! 
from pyb import Pin
from machine import I2C
from grove_lcd import Lcd

i2c = I2C(scl = Pin('D15'), sda = Pin('D14'))
lcd = Lcd(i2c,16,2)

lcd.clear()
lcd.print("Hello")
lcd.setCursor(0,1)
lcd.print("Pyboard")
