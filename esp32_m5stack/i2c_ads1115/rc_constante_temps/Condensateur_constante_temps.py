# Charge condensateur - I2C ADC 16 bits ADS1115

from machine import I2C, Pin
from ads1x15 import ADS1115
import time

################ Paramétrage CAN I2C ADS1115 ####################
i2c = I2C(freq=400000,sda=21,scl=22)
adc = ADS1115(i2c,0x48,0)

# adc = ADS1115(i2c, address, gain)
# Gain value - 0 as default
# 0 : 6.144V # 2/3x
# 1 : 4.096V # 1x
# 2 : 2.048V # 2x
# 3 : 1.024V # 4x
# 4 : 0.512V # 8x
# 5 : 0.256V # 16x

###################### Déclaration ############################## 
pinE = Pin(2, Pin.OUT) # Source de tension E du circuit RC
t = []                 # Tableau temps
N = []                 # Tableau N

################# Début charge du condensateur ##################
pinE.value(1)            # E = Vcc
to = time.ticks_ms()  # Instant initial
N.append(adc.read(7))

######################### Mesures ###############################
while N[-1] < 11271 :  # 17659 x 0.63
    t.append(time.ticks_diff(time.ticks_ms(), to))
    N.append(adc.read(7))    # Rate 0 à 7 (voir doc)

################# Affichage données en CSV ######################
print('t;N')
print('ms;_')
for i in range(len(t)) :
    print(t[i], ';', N[i])
    #U = N*6.105/32767  # Real value

print('tau = ', t[-1], 'ms')
    
################# Decharge du condensateur ######################
pinE.value(0)          # E = 0 V

################### Fermeture port I2C ##########################
i2c.deinit() # Close I2C