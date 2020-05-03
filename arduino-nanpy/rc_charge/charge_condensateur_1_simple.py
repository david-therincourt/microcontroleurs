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
x = []                          # Abscisse
y = []                          # Ordonnée

# Décharge du condensateur avant les mesures
uno.digitalWrite(8,0)           # Broche 8 à OV
sleep(2)                        # pendant 2 s

# Début de la charge du condensateur
uno.digitalWrite(8,1)           # Broche 8 à 5V   
for i in range(40):             # Boucle pour les mesures
    x.append(i)                 # Remplissage de x
    y.append(uno.analogRead(0)) # Mesure sur A0 et remplissage de y
    sleep(0.05)                 # Temporisation
    
# Décharge du condesateur après mesures
uno.digitalWrite(8,0)           # Broche 8 à 0V  

port.close()                    # Fermeture du port série

# Tracé de la courbe
plt.plot(x,y,'r+')
plt.title("R = 100k et C = 4,7uF (simple)")
plt.xlabel("i")
plt.ylabel("N")
plt.ylim(0,1023)
plt.grid()
plt.show()
