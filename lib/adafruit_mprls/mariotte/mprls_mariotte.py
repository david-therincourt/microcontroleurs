# Loi de Mariotte
# Capteur de pression absolue Adafruit MPRLS
# 0 - 25 PSI (0.25% pleine échelle)
# Seringue 20 mL
# David THERINCOURT - 05/2020

from machine import I2C
from adafruit_mprls import MPRLS
from time import sleep_ms

i2c = I2C(1)        # Premier port I2C
mprls = MPRLS(i2c)  # Déclaration du capteur de pression

V = [20, 18, 16, 14, 13, 12]
P = []

# Mesures
for vol in V :
    input("Regler le volume sur : " + str(vol) + " mL")
    pression = mprls.pressure()   # Mesure en hPa
    print(pression)               # Affichage de la pression
    P.append(pression)            # Ajout de la mesure dans le tableau

# Affichage au format CVS
print("V ; P")
print("mL ; hPa")
for i in range(len(V)):
    print(V[i], ";", P[i])
