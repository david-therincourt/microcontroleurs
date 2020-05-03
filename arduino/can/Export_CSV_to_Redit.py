import numpy as np

U,N = np.loadtxt('data.csv',delimiter='\t',skiprows=1, unpack=True, comments='#')

Nb = len(U)

print("==== ====")
print("U(V) N   ")
print("==== ====")

for i in range(Nb):
    print(U[i].round(2),int(N[i]))
    
print("==== ====")