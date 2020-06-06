# MicroPython library to support Honeywell MPRLS digital pressure sensors
# The MIT License (MIT)


from time import sleep_ms


class MPRLS:
    def __init__(self, i2c, psi_min=0, psi_max=25, address=0x18):
        self.i2c = i2c
        self.address = address
        self._psimin = psi_min
        self._psimax = psi_max
        self.buffer = bytearray(4)

    def pressure(self):
        """Pressure in hPa"""
        return self.read() * 68.947572932

    def read(self):
        """Read pressure en PSI"""
        self.i2c.writeto(self.address, b'\xAA\x00\x00')    # Configuration
        sleep_ms(200)
        self.i2c.readfrom_into(self.address, self.buffer)  # Read data         
        raw_psi = (self.buffer[1] << 16) | (self.buffer[2] << 8) | self.buffer[3]
        psi = (raw_psi - 0x19999A) * (self._psimax - self._psimin)
        psi /= 0xE66666 - 0x19999A
        psi += self._psimin
        return psi




    
