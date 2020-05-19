from microbit import *
from grove_lcd import Lcd

i2c.init(freq=100000, sda=pin20, scl=pin19)
lcd = Lcd(i2c,16,2)

lcd.clear()
lcd.print("Hello")
lcd.setCursor(0,1)
lcd.print("Micro:bit")
