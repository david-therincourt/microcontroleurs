# Lecture d'un tension entre 0 et 3,3 V sur X1
from pyb import Pin, ADC
from time import sleep_ms

pinX1 = Pin('X1') # CTN branché sur la broche X1
adc = ADC(pinX1)  # Activation du CAN
Vref = 3.276       # Mesure réelle au voltmètre - 3.3 V

for i in range(10):
    N = adc.read()               # Valeur numérique CAN
    tension = N*Vref/4095         # Caclul de la tension
    print("N = ", N)             # Affichage
    print("Tension = ", tension) # Affichage
    sleep_ms(1000)               # Temporisation
    

