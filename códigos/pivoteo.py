def space(num , space):
    x = len(str(num))
    s = ""
    for i in range(space - x):
        s += " "
    return s
def pedir_matriz(nombre , fila = None , columna = None , cuadrada = False):
    if cuadrada == False:
        if fila == None:
            y = int(input("cuantas fila tiene la matriz " + nombre + ":      "))
        else:
            y = fila
        if columna == None:
            x = int(input("cuantas columnas tiene la matriz " + nombre + ":  "))
        else:
            x = columna
    else:
        x = int(input("que tamaño tiene la matriz " + nombre + ":      "))
        y = x
    matriz = []
    for i in range(y):
        matriz += [[]]
        for j in range(x):
            matriz[-1] += [float(input("cual es el valor de la posicion [" + str(i + 1) + "," + str(j + 1) + "] de la matriz " + nombre + ":  "))]
    return matriz
#A = pedir_matriz("A" , cuadrada = True)
#B = pedir_matriz("vector respuesta" , fila = len(A) , columna = 1)
#A =[[0 , 2 , 3] , [7 , -1, 20], [1 , -14 , 8]]
def pedir_matriz(nombre , fila = None , columna = None , cuadrada = False):
    if cuadrada == False:
        if fila == None:
            y = int(input("cuantas fila tiene la matriz " + nombre + ":      "))
        else:
            y = fila
        if columna == None:
            x = int(input("cuantas columnas tiene la matriz " + nombre + ":  "))
        else:
            x = columna
    else:
        x = int(input("que tamaño tiene la matriz " + nombre + ":      "))
        y = x
    matriz = []
    for i in range(y):
        matriz += [[]]
        for j in range(x):
            matriz[-1] += [float(input("cual es el valor de la posicion [" + str(i + 1) + "," + str(j + 1) + "] de la matriz " + nombre + ":  "))]
    return matriz
A = pedir_matriz("A" , cuadrada = True)
B = pedir_matriz("vector respuesta" , fila = len(A) , columna = 1)
def matriz_sin_punto(matriz , punto):
    new_matriz = []
    for i in range(len(matriz) - 1):
        new_matriz += [[None] * (len(matriz) - 1)]
    suma = [0 , 0]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != punto[0]:
                if j != punto[1]:
                    new_matriz[i - suma[0]][j - suma[1]] = matriz[i][j]
                else:
                    suma[1] = 1
            else:
                suma[0] = 1
    return new_matriz
def determinante(matriz):
    vector_suma = [0] * len(matriz)
    if len(matriz) != 2:
        for i in range(len(matriz)):
            if matriz[i][0] != 0:
                if i/2 == int(i/2):
                    vector_suma[i] = matriz[i][0] * determinante(matriz_sin_punto(matriz , [i , 0]))
                else:
                    vector_suma[i] = -matriz[i][0] * determinante(matriz_sin_punto(matriz , [i , 0]))
    else:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    numero = 0
    for i in range(len(vector_suma)):
        numero += vector_suma[i]
    return numero
def escalonar(A , B=None , mode = None):
    if mode == "p":
        num_max = A[0][0]
        pos = None
        for i in range(1 , len(A)):
            if abs(A[i][0]) > abs(num_max):
                pos = i
                num_max = A[i][0]
        if pos != None:
            swap = A[0]
            A[0] = A[pos]
            A[pos] = swap
            swap = B[0]
            B[0] = B[pos]
            B[pos] = swap
    for i in range(1 , len(A)):
        numero = - A[i][0] / A[0][0]
        for j in range(len(A)):
            A[i][j] += A[0][j] * numero
        if B != None:
            B[len(B) - len(A) + i][0] += B[0][0] * numero
    if len(A) > 2:
        if B != None:
            ret,ret_B = escalonar(matriz_sin_punto(A, [0,0]) , B=B)
        else:
            ret = escalonar(A)
    else:
        if B != None:
            return A,B
        else:
            return A
    for i in range(1 , len(A)):
        for j in range(1 , len(A)):
            A[i][j] = ret[i - 1][j - 1]
    if B != None:
        return A,ret_B
    else:
        return A
if determinante(A) != 0:
    res = escalonar(A , B=B , mode="p")
    print("Matriz escalonada:")
    for i in range(len(res[0])):
        print(res[0][i] , "=" ,res[1][i][0])
    vector_F = [0] * len(B)
    for i in range(len(B)):
        suma = res[1][len(A) - i - 1][0]
        for j in range(i):
            suma -= res[0][len(B)- i - 1][len(A) - j - 1] * vector_F[len(B) - j - 1][0]
        vector_F[len(B) - i - 1] = [suma/res[0][len(B)- i - 1][len(B)- i - 1]]
    for i in range(len(vector_F)):
        print("X" + str(i) + " =",vector_F[i])
  