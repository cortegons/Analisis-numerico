def f(fun, x):
    y = eval(fun)
    return y

def biseccion():
    fun = input("ingresa tu función")
    a = float(input("ingresa el límite inferior del intervalo"))
    b = float(input("ingresa el límite superior del intervalo"))
    tol = float(input("ingrese la tolerancia deseada"))
    iteraciones = int(input("ingrese el número máximo de iteraciones"))
    
    i = 1
    fa = f(fun, a)
    fb = f(fun, b)
    
    if fa*fb > 0:
        print("Este intervalo no contiene una raíz")
        return
    
    while i <= iteraciones:
        p = a + (b-a)/2
        fp = f(fun, p)
        print(p, "intervalo: ", "[", a, ",", b, "]")
        if fp == 0 or (b-a)/2 < tol:
            print("La solución es ", p, " después de ", i, " iteraciones")
        if fa*fp > 0:
            a = p
            fa = fp
        else:
            b = p
            fb = fp
    if i >= iteraciones:
        print("El método no converge")

biseccion()
