import numpy as np
import matplotlib.pyplot as plt
from physique import  ajustementAffine, importCsv

h, P = np.genfromtxt("data.txt", delimiter = ";", unpack = True, skip_header = 1)

a, b = ajustementAffine(h, P)
print("a=", a, "b=", b)
h_mod = np.linspace(0,max(h),50)
P_mod = a*h_mod + b

plt.plot(h_mod,P_mod, 'b')
plt.plot(h,P,'+r')  # Trace de la courbe
plt.title("Loi de la statique des fluides")
#plt.ylim(0,1700)
plt.ylabel("Pression (Pa)")
#plt.xlim(0,0.05)
plt.xlabel("h (cm)$")
plt.grid()
plt.show()          # Affichage de la courbe
