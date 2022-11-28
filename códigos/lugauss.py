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
A = [[9.1622 , 0.4505 , 0.1067 , 0.4314 , 0.8530 , 0.4173 , 0.7803 , 0.2348 , 0.5470 , 0.5470],[0.7943 , 9.0838 , 0.9619 , 0.9106 , 0.6221 , 0.0497 , 0.3897 , 0.3532 , 0.2963 , 0.7757],[0.3112 , 0.2290 , 9.0046 , 0.1818 , 0.3510 , 0.9027 , 0.2417 , 0.8212 , 0.7447 , 0.4868],[0.5285 , 0.9133 , 0.7749 , 9.2638 , 0.5132 , 0.9448 , 0.4039 , 0.0154 , 0.1890 , 0.4359],[0.1656 , 0.1524 , 0.8173 , 0.1455 , 9.4018 , 0.4909 , 0.0965 , 0.0430 , 0.6868 , 0.4468],[0.6020 , 0.8258 , 0.8687 , 0.1361 , 0.0760 , 9.4893 , 0.1320 , 0.1690 , 0.1835 , 0.3063],[0.2630 , 0.5383 , 0.0844 , 0.8693 , 0.2399 , 0.3377 , 9.9421 , 0.6491 , 0.3685 , 0.5085],[0.6541 , 0.9961 , 0.3998 , 0.5797 , 0.1233 , 0.9001 , 0.9561 , 9.7317 , 0.6256 , 0.5108],[0.6892 , 0.0782 , 0.2599 , 0.5499 , 0.1839 , 0.3692 , 0.5752 , 0.6477 , 9.7802 , 0.8176],[10.0000 , 0.4427 , 0.8001 , 0.1450 , 0.2400 , 0.1112 , 0.0598 , 0.4509 , 0.0811 , 20.0000]]
B = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
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
def escalonar(A , B=None , L = None):
    if L == None:
        L = []
        for i in range(len(A)):
            L += [[0] * len(A)]
        for i in range(len(A)):
            L[i][i] = 1
    for i in range(1 , len(A)):
        numero = - A[i][0] / A[0][0]
        L[len(L) - len(A) + i][len(L) - len(A)] = -numero
        for j in range(len(A)):
            A[i][j] += A[0][j] * numero
        if B != None:
            B[len(B) - len(A) + i][0] += B[0][0] * numero
    if len(A) > 2:
        if B != None:
            ret,ret_B,L = escalonar(matriz_sin_punto(A, [0,0]) ,B=B , L=L)
        else:
            ret,L = escalonar(A , L=L)
    else:
        if B != None:
            return A,B,L
        else:
            return A,L
    for i in range(1 , len(A)):
        for j in range(1 , len(A)):
            A[i][j] = ret[i - 1][j - 1]
    if B != None:
        return A,ret_B,L
    else:
        return A,L
def reemplazar_arriba(U , b):
    vector_F = [0] * len(b)
    for i in range(len(b)):
        suma = b[len(U) - i - 1][0]
        for j in range(i):
            suma -= U[len(b)- i - 1][len(U) - j - 1] * vector_F[len(b) - j - 1][0]
        vector_F[len(b) - i - 1] = [suma/U[len(b)- i - 1][len(b)- i - 1]]
    return vector_F
def reemplazar_abajo(L , b):
    vector_F = [0] * len(b)
    for i in range(len(b)):
        suma = b[i][0]
        for j in range(i):
            suma -= L[i][j] * vector_F[j][0]
        vector_F[i] = [suma/L[i][i]]
    return vector_F
if determinante(A) != 0:
    b = []
    for i  in range(len(B)):
      b += [[B[i][0]]]
    res = escalonar(A , B=B)
    vector_F =reemplazar_arriba(res[0] , reemplazar_abajo(res[2] , b))
    print("matriz L")
    L = res[2]
    for i in range(len(L)):
      print(L[i])
    print("matriz U")
    U = res[0]
    for i in range(len(L)):
      print(U[i])
    for i in range(len(vector_F)):
        print("X" + str(i) + " =",vector_F[i])
else:
    print("la matriz no tiene inversa")



def space(num , space):
    x = len(str(num))
    s = ""
    for i in range(space - x):
        s += " "
    return s
def guardar_txt(archivo , titulo = None , matriz = None):
    if titulo != None:
        archivo.writelines(titulo)
    if matriz != None:
        for i in range(len(matriz)):
            string = ""
            for j in range(len(matriz[i]) - 1):
                string += str(matriz[i][j]) + space(matriz[i][j] , 25)
            string += str(matriz[i][-1])
            string += "\n"
            archivo.write(string)
for i in range(len(vector_F)):
    vector_F[i] = [vector_F[i]]
