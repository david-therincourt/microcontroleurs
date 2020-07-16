# Capteur de pression différentiel MP3V5004DP
# 0-400mm H20 -> 0-3V

from pyb import Pin, ADC
from time import sleep_ms

adc = ADC(Pin("A2"))

while True:
    N = adc.read()
    P = 50*(N/4095-0.25)
    print(N, P)
    sleep_ms(1000)
    

