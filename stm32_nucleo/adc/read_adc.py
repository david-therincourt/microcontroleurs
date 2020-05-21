from pyb import Pin, ADC

adc = ADC(Pin("A0")) # Déclaration de l'ADC sur la broche A0

Vcc = 3.288          # Valeur de la tension d'alimentation (3.3 V)
N = adc.read()       # Lecture de la conversion de 0 à 4095 (12 bits)
U = N/4095*Vcc       # Calcul de la tension
print(N, U)          # Affichage