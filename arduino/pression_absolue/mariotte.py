#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:49:32 2019

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 100
from scipy.optimize import curve_fit


V,P = np.loadtxt("data.txt",delimiter=';',skiprows=1, unpack=True)

def fct(V,A,Vo):       # Vo = volume manquant contenu dans le tube
    return A/(V+Vo)

(A,Vo), pcov = curve_fit(fct,V,P)
print(A)
print(Vo)
V2 = np.linspace(0,15,100)
P2 = fct(V2,A,Vo)

plt.plot(V,P,"+",V2,P2)
#plt.grid()
plt.xlabel('Volume (mL)')
plt.xlim(0,15)
plt.ylabel('Pression (kPa)')
plt.ylim(0,300)
plt.text(7,250,'P = A/(V+Vo)')
plt.text(7,230,'A = 1370 Pa.L')
plt.text(7,210,'Vo = 2,01 mL')
plt.text(7,190,'(volume additionnel dans le tube)')
plt.title("Loi de Mariotte - Courbe de P=f(V)")
plt.show()
