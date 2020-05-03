#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:43:59 2019

Caractéristique CAN STMA32 PyBoard

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 150
from scipy.stats import linregress

U = [0.004,0.500,0.996,1.517,2.017,2.493,2.985,3.267]
N = [8,629,1248,1901,2528,3122,3736,4090]
Umax = np.max(U)

a,b,rho,_,_=linregress(U,N)
Unew = np.linspace(0,Umax,100)
Nnew = a*Unew+b



#plt.vlines(0,0,5000)
#plt.hlines(0,0,4)
plt.plot(Unew,Nnew,'-b',U,N,'+r')
plt.xlabel("Tension (V)")
plt.xlim(0,4)
plt.ylabel("Nombre")
plt.ylim(0,5000)
plt.title("PyBoard STM32 - CAN N=f(U)")
plt.grid()
plt.show()