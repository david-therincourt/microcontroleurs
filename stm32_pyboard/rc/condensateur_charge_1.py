# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC
from time import sleep_ms

x = []
y = []

pinX1 = Pin('X1', Pin.OUT)   # Alimentation du circuit RC
pinX2  = Pin('X2')           # Tension condensateur
adc = ADC(pinX2)             # Activation du CAN

pinX1.low()                  # Décharge du condensateur
sleep_ms(2000)               # Attendre 2 s

pinX1.high()                 # Début de la charge

for i in range(50):          # Mesures
    x.append(i)
    y.append(adc.read())
    sleep_ms(3)

# Affichage des mesures en CSV
print("i;N")                 # Variables
print("_;_")                 # Unités
for i in x :
    print(x[i], ";", y[i])   # Mesures
