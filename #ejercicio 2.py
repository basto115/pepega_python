#ejercicio 2
numero=1
lista=[]

while numero!=0:
    try:
        numero = int(input("ingrese un numero: "))
        lista.append(numero)
        lista.sort()
        print(f"{lista}")
    
    except ValueError:
        print("debe ingresar un numero")