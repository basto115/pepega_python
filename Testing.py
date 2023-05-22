
#lista = [15, "nombre", 3.1515,True]

#print(lista[3])

#usuario = ["usernametest1","pass123","correo@correo.com","edad"]

numeros = [10,50,100,255,500]
#append  agrega un objeto en la ultima posicion
numeros.append(1000)
print(numeros)
#extra agrega un arreglo al final de la lista 
extra =[75,350,999]
numeros.extend(extra)
print(numeros)
#insert agreaga un valor en una posicion en especifica
numeros.insert(6,5000)
print(numeros)
#remove entrego valor, se busca y se elimina
numeros.remove(50)
print(numeros)
#pop elimina el ultimo registro
#pop(1) elimina la posicion del numero
numeros.pop()
print(numeros)
numeros.pop(3)
print(numeros)
#reverse invierte el orden del registro
numeros.reverse()
print(numeros)
#sort ordena los valores de menor a mayor
#sort(reverse=true) ordena los valores de mayor a menor
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)