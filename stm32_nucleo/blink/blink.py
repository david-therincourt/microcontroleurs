from pyb import LED
from time import sleep_ms

led = LED(1)

while True :
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)
    