# -*- coding: utf-8 -*-
# Mesure de la tension aux bornes d'un condensateur (version simple)
# R = 100 k  et C = 4,7 µF

from nanpy import ArduinoApi           # Gestion Arduino
from nanpy import SerialManager        # Gestion port série
from time import sleep 
import matplotlib.pyplot as plt        # Gestion du tracé de courbe

port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino

uno.pinMode("A0", uno.OUTPUT)      # Paramétrage de la broche 8 en sortie
uno.digitalWrite("A0",1)