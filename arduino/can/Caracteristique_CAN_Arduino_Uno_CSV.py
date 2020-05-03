# -*- coding: utf-8 -*-
"""
David THERINCOURT - 10/06/2019
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 150
from scipy.stats import linregress

# Importation des données
U,N = np.loadtxt('data.csv',delimiter='\t',skiprows=1, unpack=True, comments='#')
Umax=max(U)
# Regression linéaire
a, b, rho,_,_=linregress(U,N)
print(a,b,rho)

Unew=np.linspace(0,Umax,50)
Nnew=a*Unew+b



#plt.hlines(0,-1,6)
#plt.vlines(0,-100,1200)
plt.plot(Unew,Nnew,U,N,'+r')
plt.xlabel("U (V)")
plt.xlim(0,6)
plt.ylabel("N (10 bits)")
plt.ylim(0,1200)
plt.title("Arduino UNO - Caractéristique N=f(U)")
plt.grid()
plt.show()

