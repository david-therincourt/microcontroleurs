import numpy as np
import matplotlib.pyplot as plt

V, P = np.loadtxt('data.txt',delimiter=';',skiprows=2,unpack=True)

x = 1/V

plt.plot(x,P,'+r')  # Tracé de la courbe
plt.title("Loi de Mariotte")
plt.ylabel("Pression (hPa)")
plt.xlabel("1/V (mL-1)")
plt.grid()
plt.show()          # Affichage de la courbe
