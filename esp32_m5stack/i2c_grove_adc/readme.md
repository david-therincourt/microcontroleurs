# Grove ADC I2C (ADC121C021)

Attention, un pont diviseur de tension (1/2) composée de 2 résistances 10k (1%) est présent à l'entrée. Ce qui pose des problèmes de chute de tension pour certains capteurs (ex. CTN)

## Port I2C


	from machine import I2C
	i2c = I2C(freq=400000, sda=21, scl=22)  # freq : 100kHz ou 400 kHz

Le mode High Speed (3.4 MHz) ne fonctionne pas sur l'ESP32 !

## Adresses des registres de l'ADC121C021

	RESULT   0x00  -> Résultat de la mesure
	ALERT    0x01
	CONFIG   0x02  -> Configuration de l'ADC
	LIMITL   0x03
	LIMITH   0x04
	HYST     0x05
	CONVL    0x06
	CONVH    0x07


## Configuration

	i2c.writeto_mem(0x50,0x02,b'\x20')

* `0x50` : adresse I2C du module Grove ADC

* `0x02` : adresse registre de configuration de l'ADC.

* `\x20` : mode continu à 27 ksps.

Attention, l'écriture dans le registre se fait en binaire !

## Lecture


	Vref = 3.0
	Nbin = i2c.readfrom_mem(0x50,0x00,2)
	N = int.from_bytes(Nbin,'big')      
	U = N*2*Vref/4095

* `0x00` : adresse du registre de lecture.
* `2` : nombre d'octets (bytes) lus dans le registre (conversion sur 12 bits).

* La méthode `readfrom_men()` retourne une valeur en binaire sur deux octets d'où la conversion en décimal avec la méthode `from_bytes()`. L'option `big` permet de signifier que le premier octet est le poids fort.

* Pour plus de précision, la tension `Vref` est à ajuster (au voltmètre) en fonction du microcontrôleur.


## Fermeture port I2C

	i2c.deinit()

## Rapidité

Un test sur ESP32 M5Stack donne une période d'échantillonnage de 1 ms. Voir résultat si dessous.

	1017 µs - 908 - 1.37 V
	1817 µs - 909 - 1.371 V
	2564 µs - 910 - 1.373 V
	3293 µs - 909 - 1.371 V
	4125 µs - 911 - 1.374 V
	4891 µs - 910 - 1.373 V
	5635 µs - 911 - 1.374 V
	6363 µs - 912 - 1.376 V
	7149 µs - 912 - 1.376 V
	7908 µs - 912 - 1.376 V