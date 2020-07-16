# -*- coding: utf-8 -*-
from nanpy import ArduinoApi, SerialManager
from time import sleep                       # Importation fonction sleep()

port = SerialManager(device='/dev/ttyACM0')  # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)            # Déclaration de la carte Arduino Uno

pinLed = 2                            # Led branchée sur broche 11
uno.pinMode(pinLed,uno.OUTPUT)         # Broche Led en sortie

for i in range(100):                   # Boucle : répéter 100 fois
    uno.digitalWrite(pinLed,1)         # Led allumée
    sleep(1)                           # Attendre 1 s
    uno.digitalWrite(pinLed,0)         # Led eteinte
    sleep(1)                           # Attendre 1 s