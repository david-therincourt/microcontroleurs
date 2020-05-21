# Simple Grove I2C LCD V1.0 for MicroPython Micro:bit

import time

class Lcd():
    """This is a port of the rgb_lcd.h and rgb_lcd.cpp from the grove seeduino arduino library"""
    def __init__(self, i2c, cols, lines, dotsize = 0x00, address = 0x3e ):
        self.i2c = i2c
        self.address = address
        self._displayfunction = 0
        self._displaycontrol = 0
        self._displaymode = 0
        self._initialized = 0
        self._numlines = lines
        self._currline = 0
        
        if lines > 1:
            self._displayfunction |= 0x08
        if (not dotsize == 0) and lines == 1:
            self._displayfunction |= 0x04
        
        time.sleep(0.05)
        self.command(0x20 | self._displayfunction)
        time.sleep(0.0045)
        self.command(0x20 | self._displayfunction)
        time.sleep(0.00015)
        self.command(0x20 | self._displayfunction)
        self.command(0x20 | self._displayfunction)
        self._displaycontrol = 0x04 | 0x00 | 0x00
        self.display()
        self.clear()
        self._displaymode = 0x02 | 0x00
        self.command(0x04 | self._displaymode)
    
    def display(self):
        """turn the display on (quickly)"""
        self._displaycontrol |= 0x04
        self.command(0x08 | self._displaycontrol)

    def clear(self):
        """clear display, set cursor pos to zero"""
        self.command(0x01)
        time.sleep(0.002) #takes a while (2 microseconds wait)

    def home(self):
        """set cursor position to zero"""
        self.command(0x02)
        time.sleep(0.002) #wait 2 milliseconds to execute

    def setCursor(self, col, row):
        """puts cursor at specified location"""
        position = col | 0x80 if row == 0 else col | 0xc0
        dta = bytearray(2)
        dta[0] = 0x80
        dta[1] = position
        self.i2c.write(self.address, dta)

    def createChar(self,location,charmap):
        """allows us to fill the first 8 CGRAM locations with custom characters"""
        location &= 0x7 #essentially the same as modulo operation
        self.command(0x40 | (location << 3))
        dta = bytearray(9)
        dta[0]=0x40
        for i in range(8):
            dta[i+1] = charmap[i]
        self.i2c_send_bytes(dta)


    def command(self, value):
        """send command"""
        dta = bytearray(2)
        dta[0] = 0x80 #command register address
        dta[1] = value #command byte
        self.i2c_send_bytes(dta)

    def write(self, value):
        """send data"""
        dta = bytearray(2)
        dta[0] = 0x40 #data register address
        dta[1] = value #data byte
        self.i2c_send_bytes(dta)
        return 1 #assume success #also, I don't know why this is the only return in the other source, but there ya go.

    def i2c_send_bytes(self,dta):
        """send a bytearray 'dta' to the lcd address. use setReg for rgb address data transfers"""
        self.i2c.write(self.address, dta)

    def print(self, thing):
        """uses str() function on 'thing' and then writes it byte by byte to the lcd"""
        sthing = str(thing)
        for char in sthing:
            self.write(ord(char))
