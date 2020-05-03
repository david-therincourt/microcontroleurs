# Test DFRobot Gravity I2C ADC 16 bits ADS1115
#


from machine import I2C
from ads1x15 import ADS1115

import time

from m5stack import lcd, buttonA



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

lcd.font(lcd.FONT_DejaVu24)
lcd.clear()
lcd.text(lcd.CENTER, 0,'DFRobot Gravity')
lcd.text(lcd.CENTER,30,'I2C ADC 16 bits')
lcd.text(40,210,'Stop')


while not buttonA.wasPressed():
    N = adc.read()
    print(N)
    lcd.text(20,90,'N= %d        ' %N)
    U = N*6.105/32767  # 6.144V - valeur réelle 6.105 V sur 11 bits
    print(U)
    lcd.text(20,120,'U= %.3f V   ' %U)
    B=(0.08*U-0.2)*1000
    lcd.text(20,150,'B= %.2f mT   ' %B)
    time.sleep_ms(500)

lcd.text(lcd.CENTER,180,"** Fin **")
lcd.textClear(40,210,'Stop')
i2c.deinit() # Close I2C