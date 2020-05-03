# -*- coding: utf-8 -*-
# Mesure de la tension aux bornes d'un condensateur (version simple)
# R = 100 k  et C = 4,7 µF

from nanpy import ArduinoApi           # Gestion Arduino
from nanpy import SerialManager        # Gestion port série
from time import sleep 
import matplotlib.pyplot as plt        # Gestion du tracé de courbe
import numpy as np
from scipy.optimize import curve_fit

port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino

uno.pinMode(8, uno.OUTPUT)      # Paramétrage de la broche 8 en sortie
n = 30                          # Nombre de points de mesure
temps = np.zeros(n)             # Tableau temps
y = np.zeros(n)                 # Tableau ordonnée

# Décharge du condensateur avant les mesures
uno.digitalWrite(8,0)           # Broche 8 à OV
sleep(2)                        # pendant 2 s

# Début de la charge du condensateur
t0 = uno.millis()               # Instant initial
uno.digitalWrite(8,1)           # Broche 8 à 5V 


for i in range(n):
    temps[i] = uno.millis()
    y[i] = uno.analogRead(0)           # Lecture tension sur A1 puis affichage
    sleep(0.1)

# Décharge du condesateur après mesures
uno.digitalWrite(8,0)           # Broche 8 à 0V

port.close()                    # Fermeture du port série

# Calculs des variables
t = temps - t0
u = y*5/1023

# Modélisation
def expo(x,A,tau,xo):                  # Definition de la fonction
    return A*(1-np.exp(-(x-xo)/tau))    # Expression du modÃ¨le

(A,tau,xo), pcov = curve_fit(expo,t,u,p0=[5,500,0]) # Determination des paramÃ¨tres du modÃ¨le
print("A = ",A)                     # Affichage de A
print("tau = ",tau)                 # Affichage de tau
print("xo = ", xo)                  # Decalage  temporel
texte = "A = " + str(round(A,2)) + " V\n" + "tau = " + str(round(tau,0)) + " ms" 

tnew = np.linspace(-10,t.max(),50)
unew = expo(tnew,A,tau,xo)

# Tracé de la courbe
plt.plot(tnew,unew)
plt.plot(t,u,'r+')
plt.title("R = 100k et C = 4,7 uF")
plt.xlabel("t(ms)")
plt.ylabel("uc(V)")
plt.text(1500,3,texte,fontsize=14)
plt.grid()
plt.ylim(0,6)
plt.show()