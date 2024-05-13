print("Semana No.12: Ejercicio 1")
c=0
d=0
def MoverPosicion(cantC, cantD):
    global c, d
    c += cantC
    d += cantD
opcion= 'f'
while(opcion != 'i'):
    print("Menú")
    print("f.AREA TRIANGULO", "g.AREA CUADRADO","h.AREA RECTÁNGULO", "i.AREA CÍRCULO", sep= "\t\n")
    opcion=input("Ingrese su opción: ")

    match opcion:
        case 'f':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        case 'g':
            L = int(input("Ingrese un número entero para lado: "))
            calculoG = L*L
            print("El area del cuadrado es de:", calculoG)
        case 'h':
            b2 = int(input("Ingrese un número entero para base: "))
            a = int(input("Ingrese un número entero para altura: "))
            calculoH = b2*a
            print("El area del rectángulo es de:", calculoH)
        case 'i':
            r = int(input("Ingrese un número entero para radio: "))
            calculoI = 3.14*r*r
            print("El area del círculo es de:", calculoI)