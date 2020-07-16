
import matplotlib.pyplot as plt
import numpy as np

from physique.pyboard import Pyboard

pyboard = Pyboard("/dev/ttyACM0") # Port série de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.execFileToData("rc_charge.py")


t = np.array(x)
u = np.array(y)

max, min = u[-1], u[0]
seuil = (max-min)*0.63+min

for i in range(len(u)) :
    if u[i]>seuil :
        tau = t[i]
        break

R = 47    # kohm
C = tau/R # nF
print("Tau = ", tau, "C = ", C)

plt.plot(t,u,'r.')
plt.title("C = 10 nF et R = 47 k$\Omega$")
plt.xlabel("t(ms)")
plt.ylabel("A0")
plt.grid()
plt.xlim(-t.max()/10,t.max())
plt.ylim(0,5000)
plt.show()
