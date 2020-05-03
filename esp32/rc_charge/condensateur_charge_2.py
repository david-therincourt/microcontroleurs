# Probleme saturation ADC.
# Solution DAC comme tension de charge !!!

from machine import ADC, DAC, Pin
from time import sleep_ms

pinE = DAC(Pin(25)) 
adc = ADC(Pin(35))
#adc.atten(ADC.ATTN_11DB)
#adc.width(ADC.WIDTH_12BIT)

pinE.write(75)

for i in range(100) :
    N = adc.read()
    print(i, ";", N)
    sleep_ms(2)

pinE.write(0)

# 10 bit > 975
# 12 bit > 3900
#adc.deinit()
