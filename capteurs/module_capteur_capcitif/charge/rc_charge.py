# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
T = 2    # microsecond
f = 1E6/T
nb = 2000



pinE = Pin('A1', Pin.OUT)   # Alimentation du circuit RC
adc = ADC(Pin('A0'))             # Activation du CAN
buf = array.array("h", nb * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)         # create a timer running at 10Hz


pinE.off()                  # Décharge du condensateur
sleep_ms(1000)              # Attendre 2 s
Nmin = adc.read()
pinE.on()                 # Début de la charge
adc.read_timed(buf, tim)     # Mesures

# Données
x = [i/f*1000 for i in range(nb)] # Millisecond
y = [val for val in buf]

data = x, y
print(data)
