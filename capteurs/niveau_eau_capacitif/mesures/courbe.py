import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


h, C = np.loadtxt('data1.txt',delimiter=';',skiprows=2,unpack=True)

a,b,rho,_,_ = linregress(h, C)    # Régression linéaire
print("a = ",a)                  # Affichage de coefficient directeur
print("b = ",b)                  # Affichage de l'ordonnée à l'origine
print("rho = ",rho)              # Affichage du coefficient de corrélation

h_new = np.linspace(0,17,100)       # Nouvelle abscisse
C_new = a*h_new+b                  # Ordonnées de la fonction affine

plt.title("Capteur de niveau résistif")
plt.xlabel("h(cm)")
plt.xlim(0,18)
plt.ylabel("C(nF)")
plt.ylim(0,3)
plt.plot(h_new, C_new, "b")
plt.plot(h, C, "r+")
plt.grid()
plt.show()
