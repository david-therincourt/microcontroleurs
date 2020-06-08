# MicroPython library to support Honeywell HSC I2C digital 14 bits pressure sensors
# https://sensing.honeywell.com/sensors/amplified-board-mount-pressure-sensors/TruStability-HSC-series
# David THERINCOURT - 2020
# The MIT License (MIT)

"""
Usage :
    from machine import I2C
    from honeywell_hsc import HSC
    i2c = I2C(scl="SCL", sda="SDA")     # For Adafruit Feather STM32
    hsc = HSC(i2c, p_min=0, p_max=30)   # 30 PSI absolute sensor
    pressure = hsc.read()               # Read in PSI
    print(pressure)

"""



class HSC:
    def __init__(self, i2c, p_min=0, p_max=30, address=0x28):
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
