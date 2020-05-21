# Module Grove I2C LCD V1.0

Librairie MicroPython pour afficheur [Grove LCD I2C V1.0](https://wiki.seeedstudio.com/Grove-16x2_LCD_Series/) (alimentation en 3,3 V ou 5 V).

Pas compatible avec la version RGB.

Portage à partir de la librairie [grove_RCB_LCD](https://github.com/MomentumV/CircuitPy-i2c-lcd) pour CircuitPython par Adafruit.

## Pyboard

Fonctionne avec les cartes :

* Pyboard
* Feather STM32F405 express
* Nucleo F401RE

```python
from machine import I2C
from grove_lcd import Lcd    # Librairie pour Grove I2C LCD V1.0

i2c = I2C(1)           # Premier port I2C
lcd = Lcd(i2c,16,2)    # Afficheur LCD 16x2

lcd.clear()            # Efface l'écran
lcd.print("Bonjour")   # Ecrit un texte à l'emplacement du curseur
lcd.setCursor(0,1)     # Déplace le curseur
lcd.print("Pyboard")   # Ecrit un texte à l'emplacement du curseur
```

Ne pas oublier de copier la librairie `grove_lcd.py` dans  la mémoire flash de la carte  à côté des fichiers `boot.py` et `main.py` .

## Micro:bit

Version différente pour la carte Micro:bit avec code réduit aux fonctions essentielles (problème de mémoire).

```python
from microbit import *
from grove_lcd import Lcd

i2c.init(freq=100000, sda=pin20, scl=pin19)
lcd = Lcd(i2c,16,2)

lcd.clear()
lcd.print("Hello")
lcd.setCursor(0,1)
lcd.print("Micro:bit")
```

