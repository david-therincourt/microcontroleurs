# -*- coding: utf-8 -*-
# Lecture d'une tension sur l'entréé analogique A0  

from nanpy import ArduinoApi           # Gestion Arduino
from nanpy import SerialManager        # Gestion port série
from time import sleep                 # Importation de sleep(seconde)


port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino


for i in range(10):
    N = uno.analogRead(0)              # Lecture la valeur numérique de la tension sur A0
    print("N = ", N)                   # Affichage
    U = N*5/1023                       # Calcul de la tension en volt
    print("U = ", round(U,2), " V")    # Affichage
    sleep(1)                           # Temporisation d'une seconde

port.close()                           # Fermeture du port série
