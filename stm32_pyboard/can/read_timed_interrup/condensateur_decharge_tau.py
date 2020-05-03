# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC, Timer, ExtInt
from time import sleep_ms
import array

T = 1    # millisecond
f = 10**3/T
nb = 100




pinX1 = Pin('X1', Pin.OUT)   # Alimentation du circuit RC
pinX2  = Pin('X2')           # Tension condensateur
adc = ADC(pinX2)             # Activation du CAN

buf = array.array("h", nb * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)         # create a timer running at 10Hz
mesures = lambda e: adc.read_timed(buf, tim)             # read analog values into buf
ext = ExtInt(Pin('X3'), ExtInt.IRQ_FALLING, Pin.PULL_NONE, mesures)

pinX1.low()                  # Décharge du condensateur
sleep_ms(1000)               # Attendre 2 s
pinX1.high()                 # Début de la charge
sleep_ms(1000)
ext.disable()

x = [i*1/f*1000 for i in range(nb)]
y = [val for val in buf]
for i in range(len(x)):
    if y[i]<(max(y)*0.37):
        tau = x[i]
        break
    else:
        tau = 0

data = x, y, tau
print(data)
