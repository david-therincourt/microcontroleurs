# Charge d'un condensateur à travers une résistance
# R = 100 k et C = 220 nF

from pyb import Pin, ADC
from time import sleep_ms, ticks_ms, ticks_diff

x = []
y = []
nbPoints = 50               # Nombre de points de mesure

Vcc = 3.276
pinX1 = Pin('X1', Pin.OUT)  # Alimentation du circuit RC
pinX2  = Pin('X2')          # Tension condensateur
adc = ADC(pinX2)            # Activation du CAN


pinX1.low()                 # Décharge du condensateur
sleep_ms(2000)              # Attendre 2 s


start = ticks_ms()          # temps initial
pinX1.high()                # Début de la charge

# Mesures
for i in range(nbPoints):
    x.append(ticks_diff(ticks_ms(), start)) # Temps
    y.append(adc.read()*Vcc/4095)           # tension
    sleep_ms(3)                             # Temporisation

# Affichage des mesures en CSV
print("t;uc")                 # Variables
print("ms;V")                 # Unités
for i in range(nbPoints) :
    print(x[i], ";", y[i])    # Mesures
