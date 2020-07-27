# Microbit display
from microbit import *

display.clear()              # Efface l'afficheur
display.set_pixel(2,3,9)     # Allume la LED à la position 2,3
val = display.get_pixel(1,1) # Retourne l'intensité d'une LED
print(val)                   # Affichage de l'intensité