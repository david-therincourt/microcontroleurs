from pyb import Pin, ADC, Timer
from array import array

f = 500                           # Fréquence d'échantillonnage (750 kHz max.)
N = 20                            # Nombre de points
mesures = array("h", N*[0xFFFF])  # Tableau de N x 16 bit pour stocker les mesures
                                  # "h" pour signed short (int 2 octets)
                                        
adc = ADC(Pin('A0'))              # Déclaration du CAN sur la broche A0

tim = Timer(6, freq=f)            # Le timer 6 fixe la fréquence d'échantillonnage f

adc.read_timed(mesures, tim)      # Lancement des mesures

print(mesures)                    # Affichage des mesures