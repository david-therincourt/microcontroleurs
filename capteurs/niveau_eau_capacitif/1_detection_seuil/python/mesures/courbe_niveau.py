import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


#h = [3, 6, 8, 10]
#C = [0.7, 1.0, 1.26, 1.48]
#h, C = [0, 3, 6, 9] , [9.87, 10.27, 11.07, 11.60] # C=10nF
#h, C = [0, 3, 6, 9] , [20, 20.66, 21.07, 21.47] # C=10nF
#h, C = [0, 3, 6, 9, 12, 15] , [0.42, 2.10, 3.67, 5.25, 7.00, 8.67] # 3x Capacimètre
h, C = [0, 3, 6, 9, 12, 15] , [21.6, 23.6, 25.2, 27.3, 29.3, 31.2] # 3x µC + 22nF u*0.368

a,b,rho,_,_ = linregress(C, h)    # Régression linéaire
print("a = ",a)                  # Affichage de coefficient directeur
print("b = ",b)                  # Affichage de l'ordonnée à l'origine
print("rho = ",rho)              # Affichage du coefficient de corrélation

C_new = np.linspace(20,35,100)       # Nouvelle abscisse
h_new = a*C_new+b                  # Ordonnées de la fonction affine

plt.title("Capteur de niveau résistif")
plt.xlabel("C(nF)")
#plt.xlim(0,3)
plt.ylabel("h(cm)")
#plt.ylim(0,18)
plt.plot(C_new, h_new, "b")
plt.plot(C, h, "r+")
plt.grid()
plt.show()
