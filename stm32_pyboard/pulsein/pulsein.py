# Mesure d'un largeur d'impulsion

from machine import Pin, time_pulse_us

pin = Pin('D13')
duree = time_pulse_us(pin,0) # (pin,pulse_level) 1s max.
print(duree/1E6," seconde")