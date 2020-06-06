from pyb import Pin, ADC
from math import log
from time import sleep_ms
from onewire import OneWire
from ds18x20 import DS18X20

adc = ADC(Pin("A0")) # Déclaration de l'ADC sur la broche A0

Ro = 9.91e3     # Resistance en série avec la CTN
A =  0.0010832035972923174
B =  0.00021723460553451255
C =  3.276999926128753e-07

# Paramétrage du capteur DS18B20
ds = DS18X20(OneWire(Pin("D6")))
roms = ds.scan()
print('found probes:', roms)

while True:
    N = adc.read()
    R = Ro*N/(4095-N)           # Calcul de la résistance de la CTN
    logR = log(R)               # Logarithme népérien de R
    Tctn = 1/(A + B*logR + C*logR**3) - 273.15  # T d'après la formule de Steinhart-Hart
    ds.convert_temp()           # Mesure sur DS18B20
    Tds = ds.read_temp(roms[0]) # Lecture de la température
    print(N, R, Tctn, Tds)      # Affichage
    sleep_ms(2000)