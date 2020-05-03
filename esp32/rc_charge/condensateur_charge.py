# Un catastrophe ! Valeur pas stable du tout.

from machine import ADC, Pin
from time import sleep_ms

pinE = Pin(25, Pin.OUT) 
adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

pinE.value(1)

for i in range(50) :
    N = adc.read()
    print(i, ";", N)
    sleep_ms(3)

pinE.value(0)

# 10 bit > 975
# 12 bit > 3900
#adc.deinit()
