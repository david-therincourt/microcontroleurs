# Test d'un capteur de pression absolue Adafruit MPRLS
# 0 - 25 PSI (0.25% pleine échelle)
# David THERINCOURT - 05/2020

from machine import I2C
from adafruit_mprls import MPRLS
from time import sleep_ms

i2c = I2C(scl="SCL", sda="SDA")  # Premier port I2C
mprls = MPRLS(i2c)               # Déclaration du capteur de pression

while True:
    p = mprls.read_hPa()  # Mesure en hPa
    print(p, "hPa")       # Affichage
    sleep_ms(1000)        # Temporisation