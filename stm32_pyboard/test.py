# Mesure de la resistance d'une CTN

from pyb import Pin, ADC, delay


adc = ADC(Pin("A0")) # Déclaration du CAN

Ro = 10e3 # Résistance série

while True:
    N = adc.read() # Mesure de la tension
    R = Ro*N/(4095-N) # Calcul de R
    print("R =", R) # Affichage
    delay(1000) # Temporisation