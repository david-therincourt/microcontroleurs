# Ecrit ton programme ici ;-)
from microbit import *

while True:
    N = pin1.read_analog()
    print(N)
    U = N*3.069/1023
    print(U)
    sleep(1000)
