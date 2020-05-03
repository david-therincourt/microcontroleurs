#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:56:39 2020

@author: david
"""


import matplotlib.pyplot as plt        # Gestion du tracé de courbe
import numpy as np

t,uc = np.loadtxt('data2.txt',delimiter=';',skiprows=2,unpack=True)

# Tracé de la courbe
plt.plot(t,uc,'r+')
plt.title("R = 100 k et C = 22 nF (Pyboard)")
plt.xlabel("t (ms)")
plt.ylabel("uc (V)")
plt.ylim(0,3.5)
plt.grid()
plt.show()
