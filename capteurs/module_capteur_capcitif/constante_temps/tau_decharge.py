# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
Te = 1       # microsecond
f = 1E6/Te  # Hz
nb_mes = 1000

pinE = Pin('A1', Pin.OUT)   # Alimentation du circuit RC
adc = ADC(Pin('A0'))             # Activation du CAN
buf = array.array("h", nb_mes * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)         # create a timer running at 10Hz

pinE.on()                  # Décharge du condensateur
sleep_ms(1000)               # Attendre 2 s
Nmax = adc.read()
Nseuil = int(Nmax*0.37)
pinE.off()                 # Début de la charge

adc.read_timed(buf, tim)     # Mesures

for i in range(len(buf)):
    if buf[i]<Nseuil:
        tau = i/f*1000
        Nb_pts = i
        break
R = 100
C = tau/R*1000 # nF
print(Nmax, Nb_pts, tau, "ms", C)
    