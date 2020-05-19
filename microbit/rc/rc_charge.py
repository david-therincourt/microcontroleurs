# Programme de test de période d'une boucle
# Linéarité des intervalles de temps dans le grapheur de Mu Code

from microbit import *
from utime import ticks_ms

Dt = 10
t = []
u = []

# Décharge
pin14.write_digital(0)
sleep(2000)

# Début Charge
to = ticks_ms()
pin14.write_digital(1)

for i in range(60):
    t.append(ticks_ms()-to)
    u.append(pin0.read_analog())
    sleep(Dt)
    
for i in range(50):
    print("temps", t[i], "tension",u[i])


