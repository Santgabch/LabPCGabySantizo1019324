print("Semana No.12: Ejercicio 2")
x=0
y=0

def MoverPosicion(cantX, cantY):
    global x, y
    x += cantX
    y += cantY
opcion= 'a'
while(opcion != 'e'):
    print("Menú")
    print("a.SUBE", "b.BAJA","c.IZQUIERDA", "d.DERECHA", "e:SALIR", sep= "\t\n")
    opcion=input("Ingrese su opción: ")

    match opcion:
        case 'a':
            MoverPosicion(0,1)
        case 'b':
            MoverPosicion(0,-1)
        case 'c':
            MoverPosicion(-1,0)
        case 'd':
            MoverPosicion(1,0)
        case _:
            print("Error: debe de ingresar una letra a-e")

    print(f"La posicion actual es: [{x}][{y}]")