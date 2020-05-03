# Ecrit ton programme ici ;-)
#
from machine import Pin, time_pulse_us
from utime import sleep, sleep_us

from m5stack import lcd, buttonA

lcd.font(lcd.FONT_DejaVu24)
lcd.clear()
lcd.text(lcd.CENTER, 0,'Telemetre')
lcd.text(lcd.CENTER,30,'Module HC-SR04')
lcd.text(40,210,'Stop')

# Prise GROVE B : 36 (Echo) / 26 (Trig) / Vcc / GND
trig = Pin(26,Pin.OUT)
echo = Pin(36,Pin.IN)

trig.value(0)

while not buttonA.wasPressed():
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    duree = time_pulse_us(echo,1)
    distance = 345*duree*1E-6/2
    lcd.text(20,90, 'Dt = %d us    ' %duree)  # Durée
    lcd.text(20,120,'D = %.3f m    ' %distance)
    sleep(1)

lcd.text(lcd.CENTER,180,"** Fin **")
lcd.textClear(40,210,'Stop')
    
