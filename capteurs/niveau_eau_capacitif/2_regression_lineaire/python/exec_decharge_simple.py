# R = 10 k

import matplotlib.pyplot as plt
import numpy as np
from physique.pyboard import Pyboard
from scipy.stats import linregress

pyboard = Pyboard("/dev/ttyACM1") # Port seie de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.execFileToData("rc_decharge.py")
#exportTxt((x,y),'data_15.txt')

t = np.array(x)
u = np.array(y)
y = np.log(u)


a,b,rho,_,_ = linregress(y,t)    # RÃ©gression linÃ©aire
print("a = ",a)                  # Affichage de coefficient directeur
print("b = ",b)                  # Affichage de l'ordonnÃ©e Ã  l'origine
print("rho = ",rho)              # Affichage du coefficient de corrÃ©lation

R = 10                           # R=10k
C = -a/R                        # capacite en nF
print("C=",C)

plt.plot(t,y,'r')
plt.title("Capteur niveau eau - R = 10 k")
plt.xlabel("t(µs)")
plt.ylabel("uc")
plt.grid()

plt.show()
