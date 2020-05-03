#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:56:39 2020

@author: david
"""


import matplotlib.pyplot as plt        # Gestion du tracé de courbe
import numpy as np
from scipy.optimize import curve_fit

t, N = np.loadtxt('data.txt',delimiter=';',skiprows=2,unpack=True)

# Modélisation
def expo(x,A,tau,xo):                  # Definition de la fonction
    return A*(1-np.exp(-(x-xo)/tau))    # Expression du modÃ¨le

(A,tau,xo), pcov = curve_fit(expo,t,N,p0=[5,500,0]) # Determination des paramÃ¨tres du modÃ¨le
print("A = ",A)                     # Affichage de A
print("tau = ",tau)                 # Affichage de tau
print("xo = ", xo)                  # Decalage  temporel
texte = "Modélisation :\n" + "A = " + str(round(A,2)) + "\n" + "tau = " + str(round(tau,0)) + " ms" 
texte2 = "tau = " + str(int(t[-1])) + " ms"
tnew = np.linspace(0,5*tau,100)
Nnew = expo(tnew,A,tau,xo)

# Tracé de la courbe
plt.plot(tnew,Nnew)
plt.plot(t,N,'r.')
plt.title("R = 100 k et C = 1330 uF (ESP32 + I2C ADS1115)")
plt.xlabel("t (ms)")
plt.ylabel("uc (V)")
plt.ylim(0, 20000)
plt.xlim(0, 5*tau)
plt.text(3*tau,10000,texte,fontsize=14)
plt.plot([0,t[-1]],[N[-1],N[-1]],'k',linestyle='dashed')
plt.plot([t[-1],t[-1]],[0,N[-1]],'k',linestyle='dashed')
plt.annotate(texte2, xy=(t[-1], 0), xytext=(t[-1]*1.5,N[-1]/2), arrowprops=dict(arrowstyle="->"))
#plt.grid()
plt.show()
