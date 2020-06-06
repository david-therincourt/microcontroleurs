from pyb import Pin, ADC
from time import sleep_ms

adc = ADC(Pin("A0")) # Déclaration de l'ADC sur la broche A0

Ro = 9.91e3     # Resistance en série avec la CTN

while True:
    N = adc.read()
    R = Ro*N/(4095-N)       # Calcul de la resistance de la CTN
    print(N, R)
    sleep_ms(2000)