# -*- coding: utf-8 -*-
# R = 10 k

import matplotlib.pyplot as plt
import numpy as np
from physique.pyboard import Pyboard
from scipy.stats import linregress

pyboard = Pyboard("/dev/ttyACM1") # Port série de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.execFileToData("rc_decharge.py")



t = np.array(x)
u = np.array(y)
y = np.log(u)


a,b,rho,_,_ = linregress(y, t)    # Régression linéaire
print("a = ",a)                  # Affichage de coefficient directeur
print("b = ",b)                  # Affichage de l'ordonnée à l'origine
print("rho = ",rho)              # Affichage du coefficient de corrélation

plt.plot(t,y,'r+')
plt.title("C = 22 nF - R = 10 k")
plt.xlabel("t(µs)")
plt.ylabel("uc")
plt.grid()


plt.show()
