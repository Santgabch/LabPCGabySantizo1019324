print("Semana No.11: Ejercicio 1")
n = int(input("Ingrese un numero mayor a cero"))
if(n<=0):
    print("Error, debe ser mayor a cero")

a=0
b=1
c=0

i=2
resultado= ""

if(n>0):
    resultado = str(a)

    if(n>1):
        resultado=resultado + " ," + str(b)

        while(i<n):
            c=a+b
            resultado = resultado + "," + str(c)
            a=b
            b=c
            i=i + 1
        print(resultado)
else:
    print(resultado)


print("Semana No.11: Ejercicio 2")
n2 = int(input("Ingrese un numero mayor a cero"))

if(n2<=0):
    print("Error, debe ser mayor a cero")

e = int(input("Ingrese un número entero para x: "))
t = int(input("Ingrese un número entero para a: "))

#EJERCICO A
calculoA = 0
for xa in range(1, n2 + 1):
    calculoA += 1 / xa

#EJERCICO B
calculoB = 0
for xa in range(1, n2 +1):
    calculoB += 1 / 2**xa

#EJERCICO C
calculoC = 0
for k in range(0, t + 1):
    calculoC += e**k * (t-k)


print("El resultado de A es: ", calculoA)
print("El resultado de A es: ", calculoB)
print("El resultado de A es: ", calculoC)














