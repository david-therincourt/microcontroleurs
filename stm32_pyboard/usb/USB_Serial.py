# main.py -- put your code here!
import pyb
import time
serial = pyb.USB_VCP()
while True:
	pyb.LED(4).on()
	time.sleep(1)
	pyb.LED(4).off()
	time.sleep(1)
	serial.write("Bonjour\n\r")
	
