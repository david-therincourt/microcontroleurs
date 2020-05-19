"""
Mesure d'une tension sur le port P0
Problème de précision car saturation du CAN 1023 !
"""
from microbit import *

Vcc = 3.160 # Mesure de Vcc au voltmètre

while True:
    N = pin0.read_analog()   # Lecture sur l'entrée analogique
    U = N*Vcc/1023           # Cacul de la tension
    print(N, U)              # Affichage
    sleep(2000)              # Temporisation
