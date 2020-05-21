# Grove ADC I2C (ADC121C021)

Librairie MicroPython pour  module [Grove I2C ADC V1.2](https://wiki.seeedstudio.com/Grove-I2C_ADC/) de SeeedStudio.

Convertisseur analogique-numérique (12 bits) I2C compatible 3,3 V et 5 V.

## Installation

Copier le fichier `grove_adc.py`  dans la mémoire flash du microcontrôleur. Dans le même répertoire que les fichiers `boot.py` et `main.py`.

## Exemple avec un ESP32

Lecture brute :

```python
from machine import I2C
from grove_adc import GroveADC

i2c = I2C(freq=400000, sda=21, scl=22)  # freq : 100kHz ou 400 kHz

can = GroveADC(i2c)  
N = can.read()      # Lecture sur le CAN
print(N)

i2c.deinit()
```

Lecture de la valeur de la tension en volt :

```python
from machine import I2C
from grove_adc import GroveADC

i2c = I2C(freq=400000, sda=21, scl=22)  # freq : 100kHz ou 400 kHz

can = GroveADC(i2c)
tension = can.read_voltage() # Lecture de la tension
print(tension)

i2c.deinit()
```

Pour plus de précision, il est possible de modifier la valeur de la tension de référence  du convertisseur (3.00 V par défaut) :

```python
from machine import I2C
from grove_adc import GroveADC

i2c = I2C(freq=400000, sda=21, scl=22)  # freq : 100kHz ou 400 kHz

can = GroveADC(i2c)
can.VREF = 3.085       # Mesure au voltmètre sur le point test V0.
tension = can.read_voltage()
print(tension)

i2c.deinit()
```



## Attention

Un pont diviseur de tension (1/2) composée de 2 résistances 10k (1%) est présent à l'entrée du CAN. Ce qui réduit l’impédance d’entrée du module et pose des problèmes avec certains capteurs (ex. CTN).

