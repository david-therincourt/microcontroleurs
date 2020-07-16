# Test d'un capteur de pression absolue Adafruit MPRLS
# 0 - 25 PSI (0.25% pleine échelle)
# David THERINCOURT - 05/2020

from machine import I2C
from mprls import MPRLS
from time import sleep_ms
from ht16k33_seg import Seg7x4

i2c = I2C(1)                            # Port I2C 1
mprls = MPRLS(i2c, p_min=0, p_max=1724)  # 25 psi * 68.947572932 = 1724 hPa
aff = Seg7x4(i2c, address = 0x70)



while True:
    p = mprls.read()  # Mesure en hPa
    print(p, "hPa")   # Affichage
    aff.fill(0)             # Efface l'affichage précédent
    aff.text(str(int(p)))
    aff.show()
    sleep_ms(1000)    # Temporisation
