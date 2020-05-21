from pyb import Pin
pin = Pin("D8", Pin.OUT_PP) # En sortie "classique" (push-pull)
pin.on()                    # Etat haut (3,3 V)
#pin.off()                  # Etat bas (0 V)
