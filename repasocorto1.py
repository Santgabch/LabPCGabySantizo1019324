print("Números perfectos")
numero = int(input("Ingrese un número entero positivo para verificar si es un número perfecto: "))

def numero_perfecto(num):
    n = num
    divisores = 0

    for i in range (1, n):
        if (n % i == 0):
            divisores += i

    if (divisores == n):
        print("El número sí es un número perfecto")
    else:
        print("El número no es un número perfecto")

numero_perfecto(numero)