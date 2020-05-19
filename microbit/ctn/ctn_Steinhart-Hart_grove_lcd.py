# Ecrit ton programme ici ;-)
from microbit import *
from math import log

# Coefficients de Steinhart-Hart
A = 1.0832e-3
B = 2.1723e-4
C = 3.2770e-7
Ro = 10e3

while True:
    N = pin0.read_analog()
    R = Ro*N/(1023-N)
    logR = log(R)
    T = 1/(A + B*logR + C*logR**3) - 273.15  #
    print(N,R,T)
    sleep(2000)