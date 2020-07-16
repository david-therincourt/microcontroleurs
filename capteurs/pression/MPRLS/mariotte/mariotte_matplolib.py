import numpy as np
import matplotlib.pyplot as plt
from physique import  ajustementAffine, importCsv

V, P = np.genfromtxt("data2.txt", delimiter = ";", unpack = True, skip_header = 1)

x = 1/V
a, b = ajustementAffine(x, P)
print("a=", a, "b=", b)
x_mod = np.linspace(0,max(x),50)
P_mod = a*x_mod + b

plt.plot(x_mod,P_mod, 'b')
plt.plot(x,P,'+r')  # Trace de la courbe
plt.title("Loi de Mariotte")
plt.ylim(0,1700)
plt.ylabel("Pression (hPa)")
plt.xlim(0,0.05)
plt.xlabel("$1/V\,(mL^{-1})$")
plt.grid()
plt.show()          # Affichage de la courbe
