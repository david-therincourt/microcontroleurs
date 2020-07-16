from pyb import Pin         # Gestion des broches E/S
from time import sleep_ms   # Gestion du temps

led = Pin("D5", Pin.OUT_PP) # LED sur D5 en sortie classique (push-pull)

while True :                # Boucle infinie
    led.on()                # LED allumée
    sleep_ms(500)           # Attendre 500 ms
    led.off()               # LED éteinte
    sleep_ms(500)           # Attendre 500 ms