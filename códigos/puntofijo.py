def f(fun, x):
    y = eval(fun)
    return y

def puntofijo():
    gx=input('Por favor ingrese la funcion g(x) que se usara: ')
    aprox=input('Ingrese el valor de la aproximacion inicial: ')
    iteraciones=input('Ingrese el numero maximo de iteraciones a realizar: ')
    tol=input('Ingrese la tolerancia deseada: ')
    
    i = 1
    error = tol + 1
    
    cont = aprox
    while error > tol and i < iteraciones and f(gx, aprox) != aprox:
        xn = f(gx, aprox)
        error = abs(xn - aprox)
        aprox = xn
        i = i + 1
        cont = aprox
        
    if f(gx, aprox) == aprox:
        print(aprox, " es una raíz")
    elif error < tol: 
        print(aprox, " es una aproximación a una raíz con una tolerancia igual a ", i)
    else:
        print("No se halló ninguna raíz en ", iteraciones, " iteraciones")
        
    
    puntofijo()