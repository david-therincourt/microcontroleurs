from pyb import Pin, ADC

adc = ADC(Pin("A0"))

Vcc = 3.288
N = adc.read()
U = N/4095*Vcc
print(N, U)