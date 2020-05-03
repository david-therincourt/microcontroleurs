# Probleme saturation ADC.
# Solution DAC comme tension de charge !!!

from machine import ADC, Pin
from time import sleep_ms, ticks_diff, ticks_ms

pinE = Pin(25, Pin.OUT) 
adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

t =[]
N = []

t0 = ticks_ms()
pinE.value(1)

for i in range(50) :
    t.append(ticks_diff(ticks_ms(), t0))
    N.append(adc.read())
    sleep_ms(3)

pinE.value(0)

for i in range(len(t)) :
    print(t[i], ";", N[i])

# 10 bit > 975
# 12 bit > 3900
#adc.deinit()
