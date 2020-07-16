from math import *
from math import log as ln

T1, R1 = 2.4, 25455
T2, R2 =  25, 10475
T3, R3 =  60, 3120

# calculs en kelvins
T1 = T1 + 273.15
T2 = T2 + 273.15
T3 = T3 + 273.15

# changement de variables
Y1 = 1/T1
Y2 = 1/T2
Y3 = 1/T3

L1 = ln (R1)
L2 = ln (R2)
L3 = ln (R3)

# calculs intermediaires
a = (L2-L3)/(L1-L2)*(pow (L2,3) - pow (L1,3)) + (pow (L2,3) - pow (L3,3))
b = Y2 - Y3 - ((L2-L3)/(L1-L2))*(Y1-Y2)

# calculs de A, B et C
C = b / a
B = (1/(L1-L2))*(Y1-Y2-C*(pow(L1,3) - pow(L2,3)))
A = Y1 - B*L1 - C*pow (L1,3)

#Affichages de A, B et C
print("Dans lequation 1/T = A + B*ln R + C*(ln R)^3 on sait désormais que :")
print('A = ', A)
print('B = ', B)
print('C = ', C)