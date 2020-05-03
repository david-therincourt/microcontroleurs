#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:56:39 2020

@author: david
"""


import matplotlib.pyplot as plt        # Gestion du tracé de courbe
import numpy as np

x,y = np.loadtxt('data1.txt',delimiter=';',skiprows=2,unpack=True)

# Tracé de la courbe
plt.plot(x,y,'r+')
plt.title("R = 100 k et C = 22 nF (PyBoard)")
plt.xlabel("i")
plt.ylabel("N (12 bits)")
plt.ylim(0,4500)
plt.grid()
plt.show()
