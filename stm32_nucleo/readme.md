# Nucleo 64 et MicroPython

<img src="/home/david/PRO/Github/microcontroleurs/stm32_nucleo/nucleo_F401RE.jpg" style="zoom:50%;" />

Tester sur [NUCLEO-F401RE](https://www.st.com/en/evaluation-tools/nucleo-f401re.html).

## Firmware MicroPython

* Téléchargement du firmware sur le site officiel de MicroPython :

  [https://micropython.org/download/stm32/](https://micropython.org/download/stm32/)

* Installation du firmware sur la carte :

  [MicroPython sur NUCLEO-F411RE](https://www.diveinembedded.com/2019/04/micropython-sur-nucleo-f411re.html)

## Connexion au REPL

```python
MicroPython v1.12 on 2019-12-20; NUCLEO-F401RE with STM32F401xE
Type "help()" for more information.
>>> 
```

## Utilisation

Les fonctions sont les mêmes que pour le Pyboard officielle :

[http://docs.micropython.org/en/latest/pyboard/quickref.html](http://docs.micropython.org/en/latest/pyboard/quickref.html)

### Nom des broches

Pour connaître le nom des broches de la Nucleo :

```python
>>> from pyb import Pin
>>> dir(Pin.board)
['__class__', '__name__', '__bases__', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'D0', 'D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'LED_BLUE', 'LED_GREEN', 'LED_ORANGE', 'LED_RED', 'PA0', 'PA1', 'PA10', 'PA11', 'PA12', 'PA15', 'PA2', 'PA3', 'PA4', 'PA5', 'PA6', 'PA7', 'PA8', 'PA9', 'PB0', 'PB1', 'PB10', 'PB12', 'PB13', 'PB14', 'PB15', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7', 'PB8', 'PB9', 'PC0', 'PC1', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PD2', 'PH0', 'PH1', 'SW']
```

Pour le brochage Arduino :

* Entrées/sorties digitales de `"D0"`  à `"D15"`.
* Entrées analogiques  de `"A0"`  à `"A5"`.

### Led utilisateur

La carte NUCLEO-F401RE possède une led utilisateur de couleur verte (LD2).

```python
>>> from pyb import LED
>>> led = LED(1)  # Déclaration de la Led
>>> led.on()      # Allume la Led
>>> led.off()     # Etteint la Led
>>> led.toggle()  # Change l'état de la Led
```

### Sorties digitales

```python
>>> from pyb import Pin
>>> pin = Pin('D8', Pin.OUT_PP) # Pin.OUT_PP pour sortie "classique" (push-pull)
>>> pin.on()                    # Etat haut
>>> pin.off()                   # Etat bas
```



### Entrées digitales

Lecture de niveau logique :

```python
>>> from pyb import Pin
>>> pin = Pin('D8', Pin.IN)        # Pin en entrée "classique"
>>> pin.value()                    # Lecture état
```

Activer la résistance interne de tirage vers le haut (ex. bouton poussoir) :

```python
>>> from pyb import Pin
>>> pin = Pin('D8', Pin.IN, Pin.PULL_UP)  # Pin en entrée avec tirage vers le haut
>>> pin.value()                           # Lecture état
```

### Entrées analogiques (12 bits)

``` python
>>> from pyb import Pin, ADC
>>> adc = ADC(Pin("A0"))     # Déclaration de l'ADC sur la broche A0
>>> adc.read()               # Lecture de la conversion de 0 à 4095 (12 bits)
```

Affichage de la valeur de la tension en volt :

```python
from pyb import Pin, ADC

adc = ADC(Pin("A0")) # Déclaration de l'ADC sur la broche A0

Vcc = 3.288          # Valeur de la tension d'alimentation (3.3 V)
N = adc.read()       # Lecture de la conversion de 0 à 4095 (12 bits)
U = N/4095*Vcc       # Calcul de la tension
print(N, U)          # Affichage
```

Pour plus de précision, la tension Vcc a été mesurée au voltmètre.

### Port I2C

Port I2C présent sur les broches D14 et D15 de la connectique Arduino ou sur le connecteur I2C du [shield Grove](https://wiki.seeedstudio.com/Base_Shield_V2/) compatible Arduino (Attention : mettre le commutateur sur 3,3 V).

#### Recherche des périphériques

Bien que la librairie `pyb` dispose d’une classe I2C, il est préférable d’utiliser celle de la librairie `machine` qui est commune à toutes les cartes MycroPython.

```python
>>> from machine import I2C 
>>> i2c = I2C(1) # Premier port I2C
>>> i2c.scan()   # Recherche de périphériques
```



#### Exemple : afficheur [GROVE I2C LCD V1.0](https://wiki.seeedstudio.com/Grove-16x2_LCD_Series/) 

Pas la version RGB qui n’est pas compatible 3,3 V !

```python
from machine import I2C
from grove_lcd import Lcd    # Librairie pour Grove I2C LCD V1.0

i2c = I2C(1)           # Premier port I2C
lcd = Lcd(i2c,16,2)    # Afficheur LCD 16x2

lcd.clear()            # Efface l'écran
lcd.print("Bonjour")   # Ecrit un texte à l'emplacement du curseur
lcd.setCursor(0,1)     # Déplace le curseur
lcd.print("Nucleo")    # Ecrit un texte à l'emplacement du curseur
```

Ne pas oublier de copier la librairie `grove_lcd.py` dans  la mémoire flash de la carte  à côté des fichiers `boot.py` et `main.py` .