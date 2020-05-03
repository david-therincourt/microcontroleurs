# main.py -- put your code here!
from pyb import Pin, ADC
import time

brocheCTN = Pin('X19') # CTN branché sur la broche X19
adc = ADC(brocheCTN)   # CAN activé sur la broche X19

a = -0.0291
b = 2.41

while True:
    tension = adc.read()*3.3/4095
    temperature = (tension-b)/a
    print("Tension = ",tension)
    print("Temperature =",temperature)
    time.sleep(1)
    

