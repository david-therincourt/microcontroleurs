# Charge d'un condensateur à travers une résistance
# R = 10k et C = 22 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
from machine import I2C
from ht16k33_seg import Seg7x4

i2c = I2C(1)
aff = Seg7x4(i2c, address = 0x70)

f = 750E3   # max = 750 kHz [84Mhz/4/(12+15) = 778 kHz]
nb = 1000   # Nombre de points de mesure

pinE = Pin('A2', Pin.OUT)            # Alimentation du circuit RC
adc = ADC(Pin('A3'))                 # Activation du CAN
buf = array.array("h", nb*[0x0FFF])  # h = signed short (int 2 octets)
tim = Timer(6, freq=f)
#tim = Timer(6, prescaler=0, period=120)         # create a timer running at 10Hz

while True:
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
    h = round(1.56*C-33.7,1)

    #print("C=", C, "h =", h)
    aff.fill(0)             # Efface l'affichage précédent
    aff.text(str(h))
    aff.show()
    sleep_ms(1000)
