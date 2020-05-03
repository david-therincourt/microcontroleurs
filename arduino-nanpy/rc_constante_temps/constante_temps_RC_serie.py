# -*- coding: utf-8 -*-
# Mesure de la tension aux bornes d'un condensateur (version simple)
# R = 100 k  et C = 4,7 µF

from nanpy import ArduinoApi           # Gestion Arduino
from nanpy import SerialManager        # Gestion port série
from time import sleep 
import matplotlib.pyplot as plt        # Gestion du tracé de courbe

port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino

uno.pinMode(8, uno.OUTPUT)      # Paramétrage de la broche 8 en sortie
                            # Nombre de points de mesure
t = [0]            # Tableau temps
N = [0]                 # Tableau ordonnée

# Décharge du condensateur avant les mesures
uno.digitalWrite(8,0)           # Broche 8 à OV
sleep(2)                        # pendant 2 s

# Début de la charge du condensateur
t0 = uno.millis()               # Instant initial
uno.digitalWrite(8,1)           # Broche 8 à 5V 


while N[-1] < 645 :
    t.append(uno.millis()-t0)
    N.append(uno.analogRead(0))           # Lecture tension sur A1 puis affichage

print('Tau = ', t[-1], 'ms')

# Décharge du condesateur après mesures
uno.digitalWrite(8,0)           # Broche 8 à 0V

port.close()                    # Fermeture du port série

# Tracé de la courbe

plt.plot(t,N,'r+')
plt.title("R = 100k et C = 4,7 uF")
plt.xlabel("t(ms)")
plt.ylabel("N")
plt.grid()
plt.ylim(0,1200)
plt.xlim(0,500)
plt.show()