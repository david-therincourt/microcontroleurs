"""Example script.

Edit the I2C interface constant to match the one you have
connected the sensor to.
"""

from ina219 import INA219
from machine import I2C
from m5stack import lcd, buttonA
import time

lcd.clear()
lcd.text(0,0,'DFRobot Gravity I2C Wattmeter 26V 8A')
lcd.text(50,220,'Stop')

lcd.font(lcd.FONT_DejaVu24)
lcd.clear()
lcd.text(lcd.CENTER, 0,'DFRobot Gravity I2C')
lcd.text(lcd.CENTER,30,'Wattmeter 26V/8A')
lcd.text(40,210,'Stop')

# Edit to match interface the sensor is connect to (1 or 2).
SHUNT_OHMS = 0.01
i2c=I2C(sda=21,scl=22)

ina = INA219(SHUNT_OHMS,i2c,address=0x45 )
ina.configure()

while not buttonA.wasPressed():
    U = ina.voltage()
    I = ina.current()/1000
    P = ina.power()/1000
    print("Bus Voltage: %.3f V" % U)
    print("Current: %.4f A" % I)
    print("Power: %.3f W" % P)
    print("------------------")
    lcd.text(20,90, 'U = %.2f V       ' %U)
    lcd.text(20,120,'I = %.3f A       ' %I)
    lcd.text(20,150,'P = %.2f W       ' %P)
    time.sleep_ms(1000)

lcd.text(lcd.CENTER,180,"** Fin **")
i2c.deinit()

