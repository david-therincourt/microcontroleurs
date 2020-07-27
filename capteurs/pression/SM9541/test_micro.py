# Ne fonctionne pas ! readfrom_into() ?
from microbit import i2c, sleep
from sm9541 import SM9541

i2c.init()
capt = SM9541(i2c,-40,40)

while True:
    pressure = capt.read()
    print(pressure)
    sleep(1)
