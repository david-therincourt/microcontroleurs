from pyb import Pin, ADC, Timer
import array

f = 1000
N = 100

adc = ADC(Pin('A0'))             # Activation du CAN
buf = array.array("h", N * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(1, freq=f)         # create a timer running at 10Hz

adc.read_timed(buf, tim)     # Mesures

# Données
x = [i*1/f*1000 for i in range(N)]
y = [val for val in buf]

for i in range(len(x)):
    print(x[i], y[i])