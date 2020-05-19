'''
Mesure de la température à partir de la résistance de la CTN d'un capteur Plug'uino Grove.
Pour ce capteur la CTN est réliée à Vcc d'où la relation R = Ro*(Vcc/V-1).
La température est calculée à partir de la relation approchée de Steinhart-Hart :
1/T = A + B*ln(R) + C*(ln(R))^3 en Kelvin
Les coefficients A, B et C se calculent à partir de trois valeurs de résistances pour trois températures connues.
https://fr.wikipedia.org/wiki/Relation_de_Steinhart-Hart
'''
from microbit import *
from math import log

# Coefficients de Steinhart-Hart
A = 1.0832e-3
B = 2.1723e-4
C = 3.2770e-7
Ro = 10e3

while True:
    N = pin0.read_analog() # Lecture sur l'entrée analogique
    R = Ro*(1023/N-1)       # Calcul de la resistance de la CTN
    logR = log(R)           # Logarithme népérien
    T = 1/(A + B*logR + C*logR**3) - 273.15  #
    print(N,R,T)
    display.show(round(T,1),clear=True)
    #display.scroll(round(T,1))
    sleep(2000)