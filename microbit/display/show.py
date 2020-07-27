# Microbit display
from microbit import *

display.clear()                        # Efface l'afficheur
display.show("Bonjour", delay=1000)    # Affiche lettre par lettre
display.scroll("Bonjour", delay = 500) # Fait défiler le texte