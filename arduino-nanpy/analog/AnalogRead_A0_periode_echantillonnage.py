# -*- coding: utf-8 -*-
# Lecture d'une tension sur l'entréé analogique A0
# Mesure en temps réel dans un boucle longue                                                                       #

from nanpy import ArduinoApi           # Gestion Arduino
from nanpy import SerialManager        # Gestion port série
from time import sleep                 # Importation de sleep(seconde)


port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino


t = []
N = []

t0 = uno.millis()                  # Instant initial

for i in range(20):
    t.append(uno.millis()-t0)      # Temps
    N.append(uno.analogRead(0))    # Lecture CAN sur  A0
    #sleep(1)                      # Temporisation

port.close()                           # Fermeture du port série

print("Dt ; N ; U")
print("ms ; _ ; V")
for i in range(1, len(t)) :
    print(t[i]-t[i-1], ';', N[i], ';', round(N[i]*5/1023, 2))
