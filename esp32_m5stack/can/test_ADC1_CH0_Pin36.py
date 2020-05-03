from m5stack import machine
from time import sleep


adc = machine.ADC(machine.Pin(35))
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_12BIT)

while True :
    print(adc.read()*3.238/3134)
    sleep(1)

#adc.deinit()
