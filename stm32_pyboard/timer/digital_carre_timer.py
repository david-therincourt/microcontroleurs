from pyb import Pin, Timer

out = Pin('X1') # X1 has TIM2, CH1
tim = Timer(4)              # create a timer object using timer 4
tim.init(freq=2)                # trigger at 2Hz
tim.callback(lambda t:out.toggle())
