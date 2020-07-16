from microbit import *
from math import log

Ro = 10e3
A = 1.0832e-3 # Coefficients de Steinhart-Hart
B = 2.1723e-4 # ...
C = 3.2770e-7 # ...

while True:
    N = pin0.read_analog()                       # Mesure de la tension
    R = Ro*N/(1023-N)                            # Calcul de R
    T = 1/(A + B*log(R) + C*log(R)**3) - 273.15  # Relation de Steinhart-Hart
    print("R =", R, "T =", T)                    # Affichage
    sleep(1000)                                  # Temporisation