'''
Mesure de la résistance de la CTN d'un capteur Pluguino Grove
Pour ce capteur la CTN est réliée à Vcc.
D'où la relation R = Ro*(Vcc/V-1)
'''

from microbit import *

Vcc = 3.158   # Mesure de Vcc au voltmètre
Ro = 10e3     # Resistance en série avec la CTN

while True:
    N = pin0.read_analog() # Lecture sur l'entrée analogique
    V = N*Vcc/1023         # Calcul de la tension
    R = Ro*(Vcc/V-1)       # Calcul de la resistance de la CTN
    R2 = Ro*(1023/N-1)
    print(N, R, R2)
    sleep(2000)