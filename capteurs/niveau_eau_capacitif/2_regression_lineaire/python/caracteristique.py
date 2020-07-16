import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


#h, C = [0, 3, 6, 9, 12, 15] , [22.2, 24.1, 25.8, 27.5, 29.2, 30.8] 
h, C = [0, 3, 6, 9, 12, 15] , [10.37, 12.18, 14.01, 15.89, 17.37, 19.12] 
#h, C = [0, 5, 10, 15] , [10.37, 13.49, 16.51, 19.31] 

a,b,rho,_,_ = linregress(C, h)    # Régression linéaire
print("a = ",a)                  # Affichage de coefficient directeur
print("b = ",b)                  # Affichage de l'ordonnée à l'origine
print("rho = ",rho)              # Affichage du coefficient de corrélation

C_new = np.linspace(10,20,100)       # Nouvelle abscisse
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
