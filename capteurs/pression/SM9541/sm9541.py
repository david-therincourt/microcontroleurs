# MicroPython library to support MSI SM9541 14 bits pressure sensors
# David THERINCOURT - 2020
# The MIT License (MIT)

"""
Usage :
    from machine import I2C
    from sm9541 import SM9541
    i2c = I2C(1)
    sm = SM9541(i2c,-40,40) # -40 to +40 cm H2O
    pressure = sm.read()
    print(pressure)

"""



class SM9541:
    def __init__(self, i2c, p_min, p_max, address=0x28):
        self.i2c = i2c
        self.address = address
        self.p_min = p_min
        self.p_max = p_max
        self.n_min = 1638  # 10% de 2^14
        self.n_max = 14745 # 90% de 2^14
        self.buffer = bytearray(2)

    def read(self):
        """Read pressure"""
        self.i2c.readfrom_into(self.address, self.buffer)  # Read data
        n = (self.buffer[0] << 8) | self.buffer[1]
        return (n-self.n_min)*(self.p_max-self.p_min)/(self.n_max-self.n_min) + self.p_min

class SM9541_95002D(SM9541): # Diff Pressure -40 to 40 cm H2O
    def __init__(self, i2c, address=0x28):
        SM9541.__init__(self, i2c, -392.3, 392.3 , address) # Pascal
        
class SM9541_95003D(SM9541): # Diff Pressure -100 to 100 cm H2O
    def __init__(self, i2c, address=0x28):
        SM9541.__init__(self, i2c, -980.7, 980.7 , address) # Pascal

        