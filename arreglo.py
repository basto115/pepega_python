import numpy as np

lista = [1,2,3,4,5]
print(lista)
arreglo = np.array(lista)

print(arreglo)
print("-----------------------------")
#ndim = muestra las dimensiones del arreglo
print("tiene", arreglo.ndim, "dimensiones")
print("-----------------------------")
#len(arreglo) = para ver el largo del arreglo
print(f"arreglo tiene un largo de {len(arreglo)}")
print("-----------------------------")
#slice
#start:stop:step = 1:1:1
#start:: = indicamos desde donde queremos que revise el arreglo
#:stop: = indicamos hasta donde queremos que revise
#::step = indicamos de cuanto en cuanto queremos que revise

print(arreglo[0:4:1])

print("-----------------------------")

arreglo2 = [i for i in range(1,11)]
arreglo2 = np.array(arreglo2)
print(arreglo2)

print("-----------------------------")

for i in range(len(arreglo2)):
    print(arreglo2[i])
    
print("-----------------------------")

for x in arreglo2:
    print(x)
 
print("-----------------------------")    
#arange(start,stop,step) = rellena un arreglo con valores segun la indicacion de parametros

arreglo3 = np.arange(1,11)
print(arreglo3)

print("-----------------------------")
    
#sumar valores al arreglo completo
arreglo3 += 5
print(arreglo3)

print("-----------------------------")    

#multiplicar
arreglo3*=10
print(arreglo3)

print("-----------------------------")    

#suma y resta entre arreglos
arreglo3 += arreglo2
print(arreglo3)
arreglo3 -= arreglo2
print(arreglo3)

print("-----------------------------")    
#arr3 es mayor a arr2
print(arreglo3>arreglo2)