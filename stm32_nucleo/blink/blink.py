from pyb import LED, Pin
from time import sleep_ms

led = Pin("LED_BLUE")

while True :
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)
    