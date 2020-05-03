from pyb import Pin, Timer
from time import sleep

p = Pin('X1') # X1 has TIM2, CH1
tim = Timer(2, freq=440)
ch = tim.channel(1, Timer.PWM, pin=p)


for i in range(10,90,2):
    ch.pulse_width_percent(i)
    sleep(0.5)