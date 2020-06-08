# Absolute pressure HSCDANN030PA2A3 (3,3 V) 0-30 psi I2C
# With 10k pull-up resistor for SDA and SCL
# David THERINCOURT - 2020

from machine import I2C, Pin

adr = 40
Pmin = 0
Pmax = 2068 # hPa (30 PSI)
Nmin = 1638 # 10% de 2^14
Nmax = 14745 # 90% de 2^14

i2c = I2C(scl=Pin("SCL"), sda=Pin("SDA"), freq=400000)

data = bytearray(4)   # 32 bit = Status + Data(23:16) + Data(15:8) + Data(7:0)
i2c.readfrom_into(adr, data)  # Read data

N = (data[0] << 8) | data[1]

pression = (N-Nmin)*(Pmax-Pmin)/(Nmax-Nmin) + Pmin


print(N, pression)
