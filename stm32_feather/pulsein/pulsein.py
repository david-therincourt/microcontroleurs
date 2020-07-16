# Mesure d'un largeur d'impulsion

from machine import time_pulse_us
from pyb import Pin
sw = Pin('D13')
duree = time_pulse_us(sw,0) # (pin,pulse_level,timeout in microsecond)
print(duree/1E6," seconde")