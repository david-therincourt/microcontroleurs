import numpy as np
import matplotlib.pyplot as plt

V, P = np.loadtxt('data.txt',delimiter=';',skiprows=2,unpack=True)

x = 1/V

plt.plot(x, P, '+r')
plt.title("Loi de Boyle-Mariotte")
#plt.xlim(0,0.13)
#plt.ylim(0,2300)
plt.xlabel("1/V (mL-1)")
plt.ylabel("P (hPa)")

plt.grid()
plt.show()
