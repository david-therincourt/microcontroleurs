# Loi de Mariotte
# Capteur de pression absolue Adafruit MPRLS
# 0 - 25 PSI
# Seringue 20 mL
# David THERINCOURT - 05/2020

from physique import Pyboard, exportTxt

pyb = Pyboard("/dev/ttyACM0")      # Declaration de la carte Pyboard
pyb.enter_raw_repl()               # Entre dans le mode REPL
pyb.exec("""
from machine import I2C
from mprls import MPRLS
i2c = I2C(1)        # Premier port I2C
mprls = MPRLS(i2c, p_max=1724)  # Declaration du capteur de pression
""")


V = [60,50,40,35,30,25] # V = 40 mL pour pression atmosphérique
P = []

for vol in V :
    input("Regler le volume sur : " + str(vol) + " mL")
    output = pyb.exec("print(mprls.read())")   # Lecture de la pression
    pression = eval(output)                        # Conversion de string en float
    print(pression)                                # Affichage de la pression
    P.append(pression)                             # Ajout de la mesure dans le tableau

pyb.exit_raw_repl()                # Fermeture du mode REPL
pyb.close()                        # Deconnexion de la carte Pyboard

exportTxt((V,P), fileName = "data.txt", headerLine="V;P")
