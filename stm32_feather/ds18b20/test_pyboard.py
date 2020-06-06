from pyb import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms

ds = DS18X20(OneWire(Pin("D6")))

roms = ds.scan()
print('found probes:', roms)

ds.convert_temp()
temp = ds.read_temp(roms[0])
print(temp)
