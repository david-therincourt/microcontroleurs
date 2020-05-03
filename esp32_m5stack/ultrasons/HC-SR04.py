# Ecrit ton programme ici ;-)
#
from machine import Pin, time_pulse_us
from utime import sleep, sleep_us

# Prise GROVE B : 36 (Echo) / 26 (Trig) / Vcc / GND
trig = Pin(26,Pin.OUT)
echo = Pin(36,Pin.IN)

trig.value(0)

while True:
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    duree = time_pulse_us(echo,1)
    distance = 345*duree*1E-6/2
    print(duree, 'µs')
    print(distance, 'm')
    sleep(1)
    
    
