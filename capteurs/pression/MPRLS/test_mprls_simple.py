# Test d'un capteur de pression absolue Adafruit MPRLS
# 0 - 25 PSI (0.25% pleine échelle)
# David THERINCOURT - 05/2020

from machine import I2C
from mprls import MPRLS

i2c = I2C(1)                             # Port I2C 1
mprls = MPRLS(i2c, p_min=0, p_max=1724)  # 25 psi * 68.947572932 = 1724 hPa

p = mprls.read()  # Mesure en hPa
print(p, "hPa")   # Affichage
