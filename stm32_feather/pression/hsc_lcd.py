from machine import I2C
from grove_lcd import Lcd
from honeywell_hsc import HSC
from time import sleep_ms

i2c0 = I2C(1)
lcd = Lcd(i2c0,16,2)

i2c1 = I2C(scl="RX", sda="TX")
hsc = HSC(i2c1, p_min=0, p_max=2068) # 30 PSI = 2068 hPa



while True:
    pressure = hsc.read()
    print(pressure)
    lcd.clear()
    lcd.print("Pression (hPa)")
    lcd.setCursor(0,1)
    lcd.print(round(pressure))
    sleep_ms(1000)
    

