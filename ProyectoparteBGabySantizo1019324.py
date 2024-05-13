print("Bienvenido al sistema Rafael Landivar")
lista=[]
opcion= 'a'
while(opcion != 'g'):
    print("a. CREACION CURSO", "b. EDICION CURSO","c. CREACION ALUMNO", "d. EDICION ALUMNO", "e. CALIFICACION DE CURSOS", "f. REPORTES", "g. SALIR", sep= "\t\n")
    opcion=input("Ingrese su opción: ")

    match opcion:
        case 'a':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        case 'b':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        case 'c':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        case 'd':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        case 'e':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        case 'f':
            b = int(input("Ingrese un número entero para base: "))
            h = int(input("Ingrese un número entero para altura: "))
            calculoF = b*h / 2
            print("El area del triangulo es de:", calculoF)
        