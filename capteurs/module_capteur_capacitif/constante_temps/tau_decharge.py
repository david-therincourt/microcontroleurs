# Charge d'un condensateur à travers une résistance
# R = 10k et C > 10 nF
from pyb import Pin, ADC, Timer
from time import sleep_ms
import array

f = 500E3  # 500 kHz max
n = 1000

pinE = Pin('A3', Pin.OUT)   # Alimentation du circuit RC
adc = ADC(Pin('A2'))             # Activation du CAN
u = array.array("h", n * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)         # create a timer running at 10Hz

while True :
    pinE.on()                  # Décharge du condensateur
    sleep_ms(1000)             # Attendre
    pinE.off()                 # Début de la charge
    adc.read_timed(u, tim)     # Mesures
    seuil = u[0]*0.37
    for i in range(n):
        if u[i]< seuil:
            tau = i/f*1000  # millisecond
            break
    C = tau/10*1000 # nF
    print(nb_pts, tau, "ms", C)
