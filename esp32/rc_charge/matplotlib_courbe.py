#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:56:39 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt        # Gestion du tracé de courbe

t, N = np.loadtxt('data.txt',delimiter=';',skiprows=0,unpack=True)

# Tracé de la courbe
plt.plot(t,N,'r.')
plt.title("R = 100 k et C = 330 nF (ESP32)")
plt.xlabel("t (ms)")
plt.ylabel("uc (V)")
plt.ylim(-100, 5000)
plt.grid()
plt.show()
