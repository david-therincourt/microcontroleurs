# Capteur pression différentiel SM9541 (3,3 V)
# Ref. 95-002 > -40/40cm H2O   (392.3 Pa)
# Ref. 95-003 > -100/100 cm H2O (980.7 Pa)
# With 10k pull-up resistor for SDA and SCL
# David THERINCOURT - 2020

from machine import I2C
adr = 40
Pmin = -392.3 # pression min
Pmax = 392.3  # pression max
Nmin = 1638   # 10% de 2^14
Nmax = 14745  # 90% de 2^14

i2c = I2C(1)

data = bytearray(2)   # 32 bit = Status + Data(23:16) + Data(15:8) + Data(7:0)
i2c.readfrom_into(adr, data)  # Read data
status = data[0] >> 6
if status == 0:
    N = (data[0] << 8) | data[1]
    pression = (Pmax-Pmin)/(Nmax-Nmin)*(N-Nmin) + Pmin
else:
    pression = 0
    
print(N, pression)