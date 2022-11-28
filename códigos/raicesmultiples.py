import math
def space(num , space):
    x = len(str(num))
    s = ""
    for i in range(space - x):
        s += " "
    return s
def funcion(x):
    return math.e**x - x - 1
def funcion_prima(x):
    return math.e**x - 1
def funcion_prima_prima(x):
    return math.e**x
def funcion_newton(p1 , tol , nmax):
    
    p1 = float(input("Ingresa el primer punto"))
    tol = float(input("Ingrese tolerancia"))
    nmax = int(input("Ingrese las iteraciones"))
    i = 1
    while i <= nmax:
        p = p1 - (funcion(p1)*funcion_prima(p1))/(funcion_prima(p1)**2 - funcion(p1) * funcion_prima_prima(p1))
        if abs(p - p1) < tol:
            print("iteracion " + str(i + 1) + ":")
            print("resultado = " + str(p) + space(p , 20), "error = " , str(abs(p - p1)))
            return p
        print("iteracion " + str(i) + ":")
        print("Xn+1 = " + str(p) + space(p, 20), "error = " + str(abs(p - p1)))
        i += 1
        p1 = p
    print("fracaso")
    return None

funcion_newton()