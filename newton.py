def f(fun, x):
    y = eval(fun)
    return y

def newton():
    fun = input("ingresa tu función")
    dfun = input("ingresa la derivada de tu función")
    x0 = float(input("ingresa el valor inicial"))
    tol = float(input("ingrese la tolerancia deseada"))
    iteraciones = int(input("ingrese el número máximo de iteraciones"))
    
    fx = f(fun, x0)
    dfx = f(dfun, x0)
    
    i = 1
    
    error = tol + 1
    
    while (error > tol and fx != 0 and dfx != 0 and i <= iteraciones):
        x1 = x0 - (fx/dfx)
        fx = f(fun, x1)
        dfx = f(dfun, x1)
        error = abs(x1-x0)
        x0 = x1
        
    if fx == 0:
        print(x0, " es una raíz")
    elif error < tol:
        print("no se encontró una raíz con la tolerancia indicada")
    elif dfx == 0:
        print(x0, " es una posible raíz múltiple")
    else: 
        print(x0, " es una raíz con un error de ", error, " en ", iteraciones, " iteraciones")
        
    
