# Charge d'un condensateur à travers une résistance
# R = 10k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
from array import array

f = 3000   # max = 750 kHz [84Mhz/4/(12+15) = 778 kHz]
n = 200   # nombre de points

pinE = Pin('A0', Pin.OUT)   # A0 en sortie digitale
adc = ADC(Pin('A1'))        # CAN sur A1

buffer = array("h", n*[0x7FFF])      # h = signed short (int 2 octets)
tim = Timer(6, freq=f)               # Declaration du timer

pinE.on()                            # Décharge du condensateur
sleep_ms(1000)                       # Attendre 1 s
pinE.off()                           # Début de la charge
adc.read_timed(buffer, tim)          # Acquisition

# Affichage CSV
f = tim.freq()     # Fréquence réelle utilisée par le timer
print("t;u")
print("ms;_")
for i in range(n):
    print(i/f*1E3, ";", buffer[i])

