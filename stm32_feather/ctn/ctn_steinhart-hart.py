from pyb import Pin, ADC
from math import log
from time import sleep_ms

adc = ADC(Pin("A0")) # Déclaration de l'ADC sur la broche A0

Ro = 9.91e3     # Resistance en série avec la CTN
A =  0.0010832035972923174
B =  0.00021723460553451255
C =  3.276999926128753e-07

while True:
    N = adc.read()
    R = Ro*N/(4095-N)       # Calcul de la résistance de la CTN
    logR = log(R)           # Logarithme népérien de R
    T = 1/(A + B*logR + C*logR**3) - 273.15  # T d'après la formule de Steinhart-Hart
    print(N, R, T)
    sleep_ms(2000)