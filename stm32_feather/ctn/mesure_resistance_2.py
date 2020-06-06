from pyb import Pin, ADC
from time import sleep_ms

adc = ADC(Pin("A0")) # Déclaration de l'ADC sur la broche A0

Vcc = 3.272
Ro = 9.91e3     # Resistance en série avec la CTN

while True:
    U = adc.read()*Vcc/4095
    R = Ro*U/(Vcc-U)       # Calcul de la resistance de la CTN
    print(U, R)
    sleep_ms(2000)