# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

# Décharge d'un condensateur à travers une résistance R = 10k
# Mesure de la capacité à l'aide d'une regression linéaire
# u = A*exp(-t/tau) -> ln(u) = (-1/tau)*t + ln(A)

from pyb import Pin, ADC, Timer
from array import array
from math import log
from linear_regression import linear_reg
from time import sleep_ms

f = 750E3   # max = 750 kHz [84Mhz/4/(12+15) = 778 kHz]
nb = 100    # Nombre de points de mesure

pinE = Pin('A2', Pin.OUT)             # Source du circuit RC
adc = ADC(Pin('A3'))                  # Activation du CAN
buf = array("h", nb * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)
       
while True:
    pinE.on()                         # Décharge du condensateur E=0
    sleep_ms(100)                     # Attendre 100 ms
    pinE.off()                        # Début de la charge E=Vcc
    
    adc.read_timed(buf, tim)          # Lance les mesures

    f = tim.freq()                    # Fréquence réelle utilisée par le timer
    x = [i/f*1E6 for i in range(nb)]  # Tableau des fréquence en µs
    y = [log(val) for val in buf]     # Tableau des ln(u)

    a, b = linear_reg(x,y)            # Regression linéaire      
    C = -1/(a*10)                     # Calcul de la capacité
    print("C = ", C)                  # Affichage
    
    sleep_ms(1000)
