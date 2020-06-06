# Module RC pour capteur capacitif

## Principe

Le module est composé d’un circuit RC série alimenté par un port digital du microcontrôleur tel que :

* Un état haut (3,3 V ou 5 V) chargera le condensateur ;
* Un état bas (0 V) déchargera le condensateur.

La tension aux bornes du condensateur est accessible sur une entrée analogique.

La mesure de la constante de temps permettra de calculer la valeur de la capacité C du condensateur connaissant la valeur de la résistance série R.

$\tau =  R \times C$

Sachant que l’impédance d’entrée de ‘’

