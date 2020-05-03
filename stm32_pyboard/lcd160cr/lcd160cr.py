import lcd160cr

lcd = lcd160cr.LCD160CR('X')
lcd.set_orient(lcd160cr.LANDSCAPE)
lcd.set_pos(0, 0)
#lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
lcd.set_font(1)
lcd.write('Hello MicroPython!\n\r')
lcd.write('Hi !')
print('touch:', lcd.get_touch())