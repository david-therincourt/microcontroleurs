# -*- coding: utf-8 -*-
# Lecture d'une tension sur l'entréé analogique A0
# Mesure du temps de réponse de la fonction readAnalogue dans une boucle
# Entre 5 et 10 ms

from nanpy import ArduinoApi           # Gestion Arduino
from nanpy import SerialManager        # Gestion port série

port = SerialManager(device='/dev/ttyACM0')     # Déclaration du port série
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino


for i in range(20):
    t = uno.millis()                 # Instant avant la fonction analogRead
    N = uno.analogRead(0)            # Lecture tension sur A1 puis affichage
    Dt = uno.millis()-t              # Durée 
    print("N = ", N)
    print("Dt = ", Dt, "ms")

port.close()                           # Fermeture du port série
