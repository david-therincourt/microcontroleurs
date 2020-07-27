from microbit import *

N = pin0.read_analog() # Lecture de la tension sur P0
U = N*3.3/1023         # Calcul de la tension en volt
print(N, U)            # Affichage