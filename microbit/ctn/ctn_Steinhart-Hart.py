# Ecrit ton programme ici ;-)
from microbit import *
from math import log

# Coefficients de Steinhart-Hart
A = 1.0832e-3
B = 2.1723e-4
C = 3.2770e-7
Vcc = 3.069
Ro = 10e3

while True:
    N = pin1.read_analog()
    U = N*Vcc/1023
    R = Ro*U/(Vcc-U)
    logR = log(R)
    T = 1/(A + B*logR + C*logR**3) - 273.15  #
    print((N,U,R,T))
    display.show(round(T,1),clear=True)
    #display.scroll(round(T,1))
    sleep(2000)