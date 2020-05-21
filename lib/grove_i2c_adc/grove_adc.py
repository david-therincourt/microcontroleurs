#####################################
# Grove I2C ADC (ADC121C021)
# Library for MicroPython
# David THERINCOURT
# Under MIT License
#####################################

REG_ADDR_RESULT = 0x00
REG_ADDR_ALERT = 0x01
REG_ADDR_CONFIG = 0x02
REG_ADDR_LIMITL = 0x03
REG_ADDR_LIMITH = 0x04
REG_ADDR_HYST = 0x05
REG_ADDR_CONVL = 0x06
REG_ADDR_CONVH = 0x07



class GroveADC:
    def __init__(self, i2c, address=0x50):
        self.i2c = i2c
        self.address = address
        self.VREF = 3.0          # Ajust value with VA measure on module
        self.temp = bytearray(2)
        i2c.writeto_mem(address,REG_ADDR_CONFIG,b'\x20') # Configuration

    def read(self):
        self.i2c.readfrom_mem_into(self.address, REG_ADDR_RESULT, self.temp)
        return ((self.temp[0] & 0x0f) << 8 | self.temp[1]) & 0xfff

    def read_voltage(self):
        N = self.read()
        return N*self.VREF*2/4095
