# Pilotage d'un Arduino en Python avec Nanpy

## Introduction

Nanpy est une librairie Python destinée au **pilotage** d'un Arduino à partir d'un ordinateur programmé en Python. Il est important de noter qu'il ne s'agit pas d'une programmation en Python de la carte Arduino proprement dite mais de l'ordinateur qui pilote la carte microcontrôleur !

Ici, l'Arduino est utilisée de la manière qu'une interface d'acquisition.

Avantages :

* programmation d'une carte Arduino en langage Python et non en langage C/C++ ;
* utilisation des librairies `matplolib` et `scipy` afin d'exploiter directement des mesures effectuées par le microcontrôleur. Ces possibilités sont très appréciables pour des démonstrations de cours par exemple ;

Inconvénients :

* Pas fonctionnement de l'Arduino  en mode autonome sans câble USB (c'est quand même la fonction première d'un microcontrôleur) ;
* Vitesse d’exécution du programme Python limitée par la vitesse de communication avec l'Arduino (115 200 bauds). Par exemple, la période d'échantillonnage d'un tension analogique est d'un peu moins de 10 ms (100 Hz !!!).


## Principe

Le principe de fonctionnement est le suivant :

* la communication entre l'ordinateur et l'Arduino se fait par le câble USB (port série) ;

* le programme Python est interprété sur l’ordinateur (et non le microcontrôleur) ;

* puis le microcontrôleur exécute les ordres (protocole propre à Nanpy) reçues par l’ordinateur.

## Installation

Dans un premier temps, il est nécessaire d'installer la librairie [Nanpy](https://pypi.org/project/nanpy/) pour la distribution Python installée sur l'ordinateur.

Puis, le micro-logiciel [Nanpy-firmware](https://github.com/nanpy/nanpy-firmware) (programme Arduino C/C++) est à téléverser sur la carte Arduino avec le logiciel Arduino IDE.

**Important** : avant le téléversement du firmware sur la carte, il est impératif de créer un fichier `cfg.h` dans le croquis `/nanpy-firmware-master/Nanpy/`. Un fichier d'exemple `/sample_cfg.h` est proposé dans le répertoir `/nanpy-firmware-master/`.

## Exemple

### Blink

	from nanpy import ArduinoApi, SerialManager
	from time import sleep                       # Importation fonction sleep()
	
	port = SerialManager(device='/dev/ttyACM0')  # Sélection du port série (exemple : device = 'COM6') (exemple : device = 'COM6')
	uno = ArduinoApi(connection=port)            # Déclaration de la carte Arduino Uno
	
	pinLed = 13                            # Led intégrée à la carte
	uno.pinMode(pinLed,uno.OUTPUT)         # Broche en sortie
	
	for i in range(100):                   # Boucle : répéter 100 fois
	    uno.digitalWrite(pinLed,1)         # Led allumée
	    sleep(1)                           # Attendre 1 s
	    uno.digitalWrite(pinLed,0)         # Led eteinte
	    sleep(1)                           # Attendre 1 s

### CAN

#### Lecture d'une tension analogique

Sur l'entrée A0 :

	from nanpy import ArduinoApi           # Gestion Arduino
	from nanpy import SerialManager        # Gestion port série
	from time import sleep                 # Importation de sleep(seconde)
	
	
	port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
	uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino
	
	
	for i in range(10):
	    N = uno.analogRead(0)              # Lecture la valeur numérique de la tension sur A0
	    print("N = ", N)                   # Affichage
	    U = N*5/1023                       # Calcul de la tension en volt
	    print("U = ", round(U,2), " V")    # Affichage
	    sleep(1)                           # Temporisation d'une seconde
	
	port.close()                           # Fermeture du port série

#### Période d'échantillonnage

	from nanpy import ArduinoApi           # Gestion Arduino
	from nanpy import SerialManager        # Gestion port série
	from time import sleep                 # Importation de sleep(seconde)
	
	
	port = SerialManager(device='/dev/ttyACM0')     # Sélection du port série (exemple : device = 'COM6')
	uno = ArduinoApi(connection=port)               # Déclaration de la carte Arduino
	
	
	t = []
	N = []
	
	t0 = uno.millis()                  # Instant initial
	
	for i in range(20):
	    t.append(uno.millis()-t0)      # Temps
	    N.append(uno.analogRead(0))    # Lecture CAN sur  A0
	    #sleep(1)                      # Temporisation
	
	port.close()                       # Fermeture du port série
	
	print("Dt ; N ; U")                # Affichage
	print("ms ; _ ; V")
	for i in range(1, len(t)) :
	    print(t[i]-t[i-1], ';', N[i], ';', round(N[i]*5/1023, 2))

Résultats :

	Dt ; N ; U
	ms ; _ ; V
	8 ; 673 ; 3.29
	8 ; 672 ; 3.28
	8 ; 673 ; 3.29
	9 ; 672 ; 3.28
	8 ; 673 ; 3.29
	8 ; 672 ; 3.28
	8 ; 673 ; 3.29
	8 ; 672 ; 3.28
	9 ; 673 ; 3.29
	8 ; 673 ; 3.29
	8 ; 673 ; 3.29
	8 ; 673 ; 3.29
	8 ; 672 ; 3.28
	8 ; 673 ; 3.29
	9 ; 673 ; 3.29
	8 ; 673 ; 3.29
	8 ; 673 ; 3.29
	8 ; 673 ; 3.29
	8 ; 673 ; 3.29