import pyboard
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

pyb = pyboard.Pyboard('/dev/ttyACM0',115200)
pyb.enter_raw_repl()
repl = pyb.execfile('condensateur.py')
pyb.close()

data = repl.decode()
x,y = eval(data)

t = np.array(x)
u = np.array(y)

def expo(x,A,tau,xo):                  # Definition de la fonction
    return A*(1-np.exp(-(x-xo)/tau))    # Expression du modèle


(A,tau,xo), pcov = curve_fit(expo,t,u,p0=[1,1,10]) # Determination des paramètres du modÃ¨le
print("A = ",A)                     # Affichage de A
print("tau = ",tau)                 # Affichage de tau
print("xo = ", xo)                  # Decalage  temporel
texte = "A = " + str(round(A,2)) + " V\n" + "tau = " + str(round(tau,0)) + " ms" 

tnew = np.linspace(-10,t.max(),50)
unew = expo(tnew,A,tau,xo)

# Tracé de la courbe
#plt.plot([0,tau],[0,A],'k',linestyle='dashed')     # Tangente à l'origine
#plt.plot([xo,max(t)],[A,A],'k', linestyle='dashed') # Asymptote à l'infini
plt.plot(tnew,unew)
plt.plot(t,u,'r.')
plt.title("R = 100 k et C = 1000 nF")
plt.xlabel("t(ms)")
plt.ylabel("uc(V)")
plt.text(t.max()/2,2000,texte,fontsize=14)
plt.grid()
plt.xlim(-t.max()/5,t.max())
plt.ylim(0,5000)
plt.show()