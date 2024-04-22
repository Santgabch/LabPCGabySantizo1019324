print("Escoge una de las opciones de nuestro menú: 1) DESAYUNO 2) ALMUERZO 3) CENA")

def DESAYUNO():
    print ("Huevos, frijoles, plátanos, crema y pan; acompañado de juego natural. ---------- (Q.55.00)")

def ALMUERZO():
    print ("Carne asada, papas fritas, chirmol, frijoles, cebollitas, tortillas y guacamol; acompañada de gaseosa o jugo natural. ---------- (Q.77.00)") 

def CENA():
    print("Panes universitarios, acompañado de algun postre de la pastelería de la casa. La bebida puede ser caliente o fría a tu elección. ---------- (Q.66.00)")
def TOTAL():
    print ("Su total a pagar es de")

# Función para calcular el total a pagar
def calcular_total(opciones_elegidas):
    precios = {
        "1": 55.00,
        "2": 77.00,
        "3": 60.50,
    }
    total = sum(precios[opcion] for opcion in opciones_elegidas)
    return total

# Mostrar los menús y obtener las elecciones del usuario
opciones_elegidas = []
while True:
    print("\n¿Qué menú te gustaría elegir?")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")
    print("4. Salir")
    opcion = input("Ingresa el número de tu elección: ")

    if opcion == "4":
        break
    elif opcion in ["1", "2", "3"]:
        opciones_elegidas.append(opcion)
        print("Agregado al pedido.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Calcular el total y mostrarlo
total_a_pagar = calcular_total(opciones_elegidas)
print(f"\nTotal a pagar: Q{total_a_pagar:.2f}")