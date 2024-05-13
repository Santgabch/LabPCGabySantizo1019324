import random

print("Semana No. 16: Ejercicio 1")

lista = []

for x in range(10):
    lista.append(random.randint(0,10))

opcion='a'
while(opcion !='e'):
    print("Menu")
    print("a. Mostrar números","b.Promedio", "c.Longitud","d.Posicion", "e.Salir")
    opcion=input("Ingrese su opción: ")

    match opcion:
        case 'a': #opcion mostrar numeros
            for x in range (len(lista)):
                print(f"No.{x}:{lista[x]}")
        case 'b': ##opcion promedio
            sumatoria=0
            for x in range(len(lista)):
                sumatoria+=lista[x]
            promedio = sumatoria/len(lista)
            print(f"-----Promedio:{promedio}")

        case 'c':
            longitud=len(lista)
            print("La longitud del arreglo es:", longitud)
        case 'd':
            suma_pares=0
            suma_impares=0
            for i in range(len(lista)):
                if i % 2 == 0:
                    suma_pares += lista[i]
                else:
                    suma_impares += lista[i]
            print("Suma de posiciones pares:", suma_pares)
            print("Suma de posiciones impares:", suma_impares)

print("Semana No. 16: Ejercicio 2")
cantFilas=int(input("Ingrese la cantidad de filas"))
cantCols=int(input("Ingrese la cantidad de columnas"))

matriz =[[0 for x in range(cantCols)] for y in range(cantFilas)]
mayor=float('-inf')
menor=float('inf')
for xFilas in range(cantFilas):
    for xCols in range(cantCols):
        matriz[xFilas][xCols]=random.randint(0,1000)
        #Comparación mayor
        if(matriz[xFilas][xCols] > mayor):
            mayor=matriz[xFilas][xCols]
        #Comparacion menor
        if(matriz[xFilas][xCols] < menor):
            menor = matriz[xFilas][xCols]
        #mostrar cantidad de numeros pares e impares en la matriz
        cant_pares = 0
        cant_imp=0
        for xFila in matriz:
            for numero in xFila:
                if numero % 2 ==0:
                    cant_pares +=1
                else:
                    cant_imp +=1

print(matriz)
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")
print(f"La cantidad de valores pares es: {cant_pares}")
print(f"La cantidad de valores impares es: {cant_imp}")