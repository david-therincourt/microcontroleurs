'''
Mesure de la résistance de la CTN d'un capteur Pluguino Grove
Pour ce capteur la CTN est réliée à Vcc.
D'où la relation R = Ro*(Vcc/V-1)
'''

from microbit import *

Ro = 10e3     # Resistance en série avec la CTN

while True:
    N = pin0.read_analog() # Lecture sur l'entrée analogique
    R = Ro*(1023/N-1)       # Calcul de la resistance de la CTN
    print(N, R)
    sleep(2000)