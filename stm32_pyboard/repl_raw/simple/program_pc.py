import pyboard
import matplotlib.pyplot as plt

pyb = pyboard.Pyboard('/dev/ttyACM0',115200)
pyb.enter_raw_repl()
repl = pyb.execfile('test_pyboard.py')
pyb.close()

data = repl.decode()
x,y = eval(data)
plt.plot(x,y)
plt.show()