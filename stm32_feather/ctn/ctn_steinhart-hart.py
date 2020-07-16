from pyb import Pin, ADC
from math import log
from time import sleep_ms

adc = ADC(Pin("A2")) # Déclaration de l'ADC sur la broche A0

Ro = 10e3                   # Résistance série
A =  0.0010832035972923174  # Coeff. de Steinhart-Hart
B =  0.00021723460553451255 # ...
C =  3.276999926128753e-07  # ...

while True:
    N = adc.read()                               # Mesure de la tension
    R = Ro*N/(4095-N)                            # Calcul de R_CTN
    T = 1/(A + B*log(R) + C*log(R)**3) - 273.15  # Relation de Steinhart-Hart
    print("R =", R, "T =", T)                    # Affichage
    sleep_ms(1000)                               # Temporisation