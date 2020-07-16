# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
T = 0.02    # microsecond
f = 1/(T*1E-3)
nb = 30

pinE = Pin('A2', Pin.OUT)   # Alimentation du circuit RC
adc = ADC(Pin('A3'))             # Activation du CAN
buf = array.array("h", nb * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)         # create a timer running at 10Hz


pinE.off()                  # Décharge du condensateur
sleep_ms(1000)              # Attendre 2 s
pinE.on()                 # Début de la charge
adc.read_timed(buf, tim)     # Mesures

# Données
f = tim.freq()
x = [i/f*1E3 for i in range(nb)] # Millisecond
y = [val for val in buf]

print((x,y))
