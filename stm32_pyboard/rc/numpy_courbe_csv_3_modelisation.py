#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:56:39 2020

@author: david
"""


import matplotlib.pyplot as plt        # Gestion du tracé de courbe
import numpy as np
from scipy.optimize import curve_fit

t,u = np.loadtxt('data2.txt',delimiter=';',skiprows=2,unpack=True)

def expo(x,A,tau,xo):                  # Definition de la fonction
    return A*(1-np.exp(-(x-xo)/tau))    # Expression du modèle


(A,tau,xo), pcov = curve_fit(expo,t,u,p0=[3,22,0]) # Determination des paramètres du modÃ¨le
print("A = ",A)                     # Affichage de A
print("tau = ",tau)                 # Affichage de tau
print("xo = ", xo)                  # Decalage  temporel
texte = "A = " + str(round(A,2)) + " V\n" + "tau = " + str(round(tau,0)) + " ms" 

tnew = np.linspace(-10,t.max(),50)
unew = expo(tnew,A,tau,xo)

# Tracé de la courbe
plt.plot([0,tau],[0,A],'k',linestyle='dashed')     # Tangente à l'origine
plt.plot([0,max(t)],[A,A],'k', linestyle='dashed') # Asymptote à l'infini
plt.plot(tnew,unew)
plt.plot(t,u,'r+')
plt.title("R = 100 k et C = 220 nF")
plt.xlabel("t(ms)")
plt.ylabel("uc(V)")
plt.text(80,2,texte,fontsize=14)
plt.grid()
plt.ylim(0,3.5)
plt.show()
