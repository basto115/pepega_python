#aaa

import numpy as np

arreglo = np.arange(1,101)
print(arreglo)
print("-------------")
#reshape = permite modificar la forma del arreglo
arreglo = arreglo.reshape((25,4))
print(arreglo)
print("-------------")
arreglo = arreglo.reshape((10,10))
print(arreglo)
print("-------------")
print(arreglo[5,5])
print(arreglo[5][5])   #ambos sirven
print("-------------")

#para encontrar el 100
print(arreglo[-1,-1]) 
print(arreglo[9,9])
print(arreglo.max())
print("-------------")
#slice
#start:stop:step
#mostrar desde la mitad y solo los primeros 5
print(arreglo[5::,:5:])
print("-------------")
#mostrar los primeros 3 datos de las primeras 4 filas
print(arreglo[:4,:3])
print("-------------")
#mostrar desde 61 hasta el 80

print(arreglo[6:9,:])
print("-------------")

#mostrar el ultimo digito de cada fila
print(arreglo[:,-1:])
print("-------------")

numero = int(input("ingrese un numero: "))

for y in range(10):
    for x in range(10):
        if arreglo[y,x]==numero:   
            print(f"en la fila {y} y en la columna {x} se encuentra el valor {arreglo[y,x]} ")
            
print("-------------")

#utilidades

#ndim = cuantas dimensiones tiene
print(arreglo.ndim)
print("-------------")

#shape = muestra la forma del arreglo

print(arreglo.shape)
print("-------------")

#size = muestra el largo del arreglo
print(arreglo.size)            
print("-------------")

# concatenate

arr1 = np.array([[1,2,3]],[[4,5,6]])
arr2 = np.array([[10,20,30]],[[40,50,60]])

arr3 = np.concatenate((arr1,arr2), axis=0)
print(arr3)
