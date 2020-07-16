from pyb import Pin, Timer
from time import sleep_ms

tim = Timer(3, freq=440)    
pwm = tim.channel(2, Timer.PWM, pin=Pin('D5')) # Y2 pour Pyboard
pwm.pulse_width_percent(50)

for f in [440, 560, 780]:
    tim.freq(f)
    sleep_ms(1000)
    
tim.deinit()
