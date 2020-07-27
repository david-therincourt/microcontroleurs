from pyb import Pin, Timer

led = Pin('D5', Pin.OUT_PP)              # TIM3, CH2 pour D5 ou Y2
tim = Timer(3, freq=500)                 # Timer 3 fixé à 500 Hz 
pwm = tim.channel(2, Timer.PWM, pin=led) # PWM sur la voie 2 du timer 3

pwm.pulse_width_percent(33)              # Lancement du signal - Rapport cyclique = 33%

tim.freq(400)                            # Modification de la fréquence