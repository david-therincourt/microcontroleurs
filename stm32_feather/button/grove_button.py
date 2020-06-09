# Grove button v1.2 with integrate pull down resistor
# OFF = 0 and ON = Vcc
# David THERINCOURT - 2020

from pyb import Pin
from time import sleep_ms

button = Pin('D5', Pin.IN)

while button.value()==0 :
    print("Hello")
    sleep_ms(1000)