# Test Grove I2C ADC sur ESP32 M5Stack
from machine import I2C
from grove_adc import GroveADC

i2c = I2C(freq=400000, sda=21, scl=22)  # freq : 100kHz ou 400 kHz

can = GroveADC(i2c)
can.VREF = 3.085       # 3.00 par défaut. Mesure réelle au voltmètre sur V0.
tension = can.read_voltage()
print(tension)

i2c.deinit()