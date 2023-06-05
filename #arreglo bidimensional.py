#arreglo bidimensional

import numpy as np

lista =[[1,2,3],[4,5,6],[7,8,9]]

arreglo = np.array(lista)

print(arreglo)
#print(arreglo[2][2])

#es como jugar battleship, acuerdate de eso xddd
#recorrido con doble for y para eje vertical x para eje horizontal


print("-----------------------------")    
for y in range(3):
    for x in range(3):
        print(arreglo[y][x])