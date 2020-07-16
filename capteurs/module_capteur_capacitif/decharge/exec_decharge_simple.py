#
import matplotlib.pyplot as plt
import numpy as np
from physique.pyboard import Pyboard

pyboard = Pyboard("/dev/ttyACM0") # Port série de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.execFileToData("rc_decharge.py")

t = np.array(x)
u = np.array(y)


plt.plot(t,u,'r.')
plt.title("Décharge d'un condensateur C = 1 µF à travers R = 10k$\Omega$")
plt.xlabel("t(ms)")
plt.ylabel("uc")
plt.grid()
plt.xlim(-t.max()/10,t.max())
plt.ylim(0,5000)
plt.show()
