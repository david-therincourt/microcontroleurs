# Marche bien de 10 a  50 nF
# R = 10 k

import matplotlib.pyplot as plt
import numpy as np
from physique.pyboard import Pyboard
from physique.csv import exportTxt

pyboard = Pyboard("/dev/ttyACM1") # Port seie de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.execFileToData("rc_decharge.py")
#exportTxt((x,y),'data_15.txt')

t = np.array(x)
u = np.array(y)

max, min = u[0], u[-1]
seuil = (max-min)*0.368+min
#seuil = u[0]*0.368

for i in range(len(u)) :
    if u[i]<seuil :
        tau = t[i]
        break

R = 9.93
C = tau/R # nF
h = 1.56*C-33.7


print("Tau = ", tau, "C = ", C, "h = ", h)

plt.plot(t,u,'r')
plt.title("Capteur niveau eau - R = 10 k")
plt.xlabel("t(µs)")
plt.ylabel("uc")
plt.grid()
plt.xlim(-t.max()/5,t.max())
plt.ylim(0,5000)
plt.show()
