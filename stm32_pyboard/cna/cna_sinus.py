import math
from pyb import DAC
freq=440
amp=127
# create a buffer containing a sine-wave
buf = bytearray(100)
for i in range(len(buf)):
    buf[i] = 128 + int(amp * math.sin(2 * math.pi * i / len(buf)))

# output the sine-wave at 400Hz
dac = DAC(1) # X5
dac.write_timed(buf, freq * len(buf), mode=DAC.CIRCULAR)