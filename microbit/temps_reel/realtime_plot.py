# Programme de test de période d'une boucle
# Linéarité des intervalles de temps dans le grapheur de Mu Code

from microbit import *
from utime import ticks_ms

Dt = int(input("Dt (ms) = "))
to = ticks_ms()
t = []

for i in range(20):
    t.append((0,ticks_ms()-to))
    sleep(Dt)

for ligne in t:
    print(ligne)
