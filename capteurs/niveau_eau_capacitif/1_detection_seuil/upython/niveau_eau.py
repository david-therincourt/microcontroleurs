# Charge d'un condensateur à travers une résistance
# R = 10k et C = 22 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
#T = 0.5    # microsecond
f = 750E3   # max = 750 kHz [84Mhz/4/(12+15) = 778 kHz]
nb = 1000


pinE = Pin('A3', Pin.OUT)   # Alimentation du circuit RC
adc = ADC(Pin('A2'))             # Activation du CAN
buf = array.array("h", nb*[0x0FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)
#tim = Timer(6, prescaler=0, period=120)         # create a timer running at 10Hz


pinE.on()                  # Décharge du condensateur
sleep_ms(100)             # Attendre 2 s
pinE.off()                 # Début de la charge
adc.read_timed(buf, tim)   # Mesures

seuil = buf[0]*0.368

for i in range(nb) :
    if buf[i]<seuil :
        tau = i/tim.freq()*1E6
        break

R = 9.93
C = tau/R # nF
h = 1.56*C-33.7

print("C=", C, "h =", h)
