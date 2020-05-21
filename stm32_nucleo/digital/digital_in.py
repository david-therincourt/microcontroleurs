from pyb import Pin

pin = Pin('D8', Pin.IN)               # Entrée "classique"
#pin = Pin('D8', Pin.IN, Pin.PULL_UP) # Entrée avec résistance de tirage vers le haut

valeur = pin.value()
print(valeur)
