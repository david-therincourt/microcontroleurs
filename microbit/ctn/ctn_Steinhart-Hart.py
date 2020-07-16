# Ecrit ton programme ici ;-)
from microbit import *
from math import log
from grove_lcd import Lcd

Ro = 10e3
A = 1.0832e-3 # Coefficients de Steinhart-Hart
B = 2.1723e-4 # ...
C = 3.2770e-7 # ...


i2c.init(freq=100000, sda=pin20, scl=pin19)
lcd = Lcd(i2c,16,2)

while True:
    N = pin0.read_analog()
    R = Ro*N/(1023-N)
    logR = log(R)
    T = 1/(A + B*logR + C*logR**3) - 273.15  #
    print(N,R,T)
    lcd.clear()
    lcd.print("Temperature")
    lcd.setCursor(0,1)
    lcd.print(round(T,1))
    sleep(2000)