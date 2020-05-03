from pyb import UART
from time import sleep

HC05 = UART(1,9600)

while True:
    HC05.write('Bonjour\n\r')
    sleep(1)
    
