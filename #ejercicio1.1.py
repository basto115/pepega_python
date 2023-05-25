#ejercicio1
numero = int(input("ingrese un numero: "))
lista = []
contador=0

for i in range(1,11):
    tabla = numero*i
    lista.append(tabla)
    
for x in lista:
    print(f"posicion {contador} es: {x} ")
    contador+=1