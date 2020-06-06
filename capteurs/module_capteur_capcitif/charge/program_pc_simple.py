import pyboard
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

pyb = pyboard.Pyboard('/dev/ttyACM0',115200)
pyb.enter_raw_repl()
repl = pyb.execfile('rc_charge.py')
pyb.close()

data = repl.decode()
x,y = eval(data)

t = np.array(x)
u = np.array(y)

plt.plot(t,u,'r')
plt.title("R = 100 k et C = 330 nF")
plt.xlabel("t(ms)")
plt.ylabel("uc")
plt.grid()
plt.xlim(-t.max()/5,t.max())
plt.ylim(0,5000)
plt.show()
