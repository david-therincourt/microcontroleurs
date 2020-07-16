# Loi de Mariotte en mode REPL sur PyBoard
# Capteur de pression absolue Adafruit MPRLS 0 - 25 PSI
# Seringue 60 mL
# David THERINCOURT - 05/2020

from machine import I2C
from mprls import MPRLS

i2c = I2C(1)                    # Premier port I2C
mprls = MPRLS(i2c, p_max=1724)  # 25 psi = 1724 hPa

V = [60,50,40,35,30,25]         # V=40 mL pour pression atmosphérique
P = []                          # Stockage des pressions

# Mesures
for vol in V :
    input("Régler le volume sur " + str(vol) + " mL")
    pression = mprls.read()    # Lecture de la pression
    print(pression, "hPa")     # Affichage de la pression
    P.append(pression)         # Ajout de la mesure dans le tableau

# Affichage au format CSV
print("V ; P")
print("mL ; hPa")
for i in range(len(V)):
    print(V[i],";",P[i])