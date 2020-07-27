from microbit import *
from time import ticks_ms

N  = 10                         # Nombre de points de mesures
Dt = 20                         # Période d'échantillonnage (ms)
tps = [None]*N                  # Création d'un tableau pour le temps
val = [None]*N                  # Création d'un tableau pour les mesures

to = ticks_ms()                 # Définition de l'instant initial

for i in range(10):
    tps[i] = ticks_ms()-to      # Instant de la mesure
    val[i] = pin0.read_analog() # Mesure tension sur P0
    sleep(Dt)                   # Attendre Dt
    
print(tps)
print(val)