# Charge d'un condensateur à travers une résistance
# R = 10k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
#T = 1    # microsecond
f = 1000   # max = 750 kHz [84Mhz/4/(12+15) = 778 kHz]
nb = 50


pinE = Pin('A2', Pin.OUT)   # Alimentation du circuit RC
adc = ADC(Pin('A3'))             # Activation du CAN
buf = array.array("h", nb * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)
#tim = Timer(6, prescaler=0, period=110)         # create a timer running at 10Hz


pinE.on()                  # Décharge du condensateur
sleep_ms(1000)             # Attendre 2 s
pinE.off()                 # Début de la charge
adc.read_timed(buf, tim)   # Mesures


# Données
f = tim.freq()                   # Fréquence réelle utilisée par le timer
x = [i/f*1E3 for i in range(nb)] # Microsecond
y = [val for val in buf]

print((x,y))
