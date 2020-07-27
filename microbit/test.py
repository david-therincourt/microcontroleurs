# Clignotement d'une LED sur P0
from microbit import *
from utime import sleep_ms

while True:               # Boucle sans fin
    pin0.write_digital(1) # P0 à l'état haut
    sleep_ms(500)         # Attendre 500 ms
    pin0.write_digital(0) # P0 à l'état bas
    sleep_ms(500)         # Attendre 500 ms