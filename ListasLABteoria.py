A=[[1, 4, 5],
   [-5, 8, 9]]

print("A[0] =", A[0])
print("A[1] =", A[1])

for row in A :
    for element in row:
        print(element)

for row in A :
    for element in row:
        print(element, end = ' ')
    print()


print("EJERCICIO 2")
A=[[1, 4, 5],
   [-5, 8, 9],
   [-5, 8, 9]]

B=[[1, 4, 5],
   [-5, 8, 9],
   [-5, 8, 9]]

RESULTADO=[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        RESULTADO[i][j] = A[i][j] + B[i][j]

for res in RESULTADO:
    print(res)
