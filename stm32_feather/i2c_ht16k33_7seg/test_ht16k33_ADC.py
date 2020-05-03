# Copier ht16k33_matrix.py et ht16k33_seg dans /lib de la Pyboard
# Test sur STM32F405 Feather Express

from pyb import Pin, ADC
from machine import I2C
from ht16k33_seg import Seg7x4
from time import sleep

i2c = I2C(scl = Pin('SCL'), sda = Pin('SDA'))
aff = Seg7x4(i2c, address = 0x70)


pinA0 = ADC(Pin("A0"))


while True :
    tension = round(pinA0.read()*3.3/4095, 2)
    print(tension)
    aff.fill(0)             # Efface l'affichage précédent
    aff.text(str(tension))  # Texte à afficher
    aff.show()              # Affichage
    sleep(1)
