print("Semana No.14: Ejercicio 1")

nombres=[]
# Pedir al usuario que ingrese 5 nombres
for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)

# Imprimir la lista de nombres ingresados
print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)

print("Semana No.14: Ejercicio 2")

# Crear una lista vacía para almacenar las edades
edades = []

# Pedir al usuario que ingrese 5 edades
for i in range(5):
    while True:
        try:
            edad = int(input(f"Ingrese la edad {i + 1}: "))
            if edad > 0:
                edades.append(edad)
                break
            else:
                print("La edad NO es válida, debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un número entero positivo. Inténtelo nuevamente.")

# Imprimir la lista de edades ingresadas
print("Las edades ingresadas son:")
for edad in edades:
    print(edad)
    