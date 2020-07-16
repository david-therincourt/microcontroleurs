# -*- coding: utf-8 -*-
# Mesure de la resistance d'une CTN et calcul de la température
# Calcul de la température à partir de la relation de Steinhart-Hart

from nanpy import ArduinoApi           # Gestion de l'Arduino
from nanpy import SerialManager        # Gestion port série
from time import sleep                 # Importation de sleep(seconde)
from math import log

Vcc = 5.0      # Tension d'alimentation
Ro = 10000     # Résistance du pont
A = 1.0832e-3  # Coeff. de Steinhart-Hart
B = 2.1723e-4  # ...
C = 3.2770e-7  # ...

port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino


while True :
    U = uno.analogRead(0)*5/1023       # Lecture la tension sur A0
    R = Ro*U/(Vcc-U)                   # Calcul de la résistance
    T = (1.0 / (A + B*log(R) + C*log(R)**3))
    T = T-273.15                       # Calcul de la température
    print("R = ", R, "T = ", T)        # Affichage
    sleep(1)                           # Temporisation d'une seconde

port.close()                           # Fermeture du port série
