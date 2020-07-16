from pyb import DAC

dac = DAC(1)            # DAC 1 sur la broche A0 (Feather) ou X5 (Pyboard)
dac.write(128)          # Ecriture d'une valeur sur 8 bit

dac = DAC(1, bits=12)   # DAC 1 en 12 bit
dac.write(4095)         # Ecriture de la valeur maximale