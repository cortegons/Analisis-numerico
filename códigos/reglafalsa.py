from sympy import exp, cos
import numpy as np

def regla_falsa ():
    f = input("Ingresa tu función")
    x0 = float(input("Ingresa x0"))
    x1 = float(input("Ingresa x1"))
    tol = float(input("Ingresa la tolerancia"))
    nmax = int(input("Ingresa # de iteraciones"))
    temp,err,cont,xcentro = 0,0,1,0
    xant = f(x0)
    xact = f(x1)
    if (xant == 0):
        print(x0, "es raiz")
    else:
        if (xact == 0):
            print(x1, "es raiz")
        else:
            if (xant*xact < 0):
                xcentro = x0 - (xant*(x1-x0)/(xact-xant))
                fcentro = f(xcentro)
                err = tol + 1
                print("\n-------------------------------------------------------")
                print("iteracion | xMedio | fcentro | error absoluto")
                #print(cont, "|", x0,"|",x1,"|",xcentro,"|",fcentro,"|",err)
                print(cont, "|",xcentro,"|",fcentro,"|",err)
                while((err > tol) and (fcentro != 0) and cont < nmax):
                    if (xant*fcentro < 0):
                        x1 = xcentro
                        xact = fcentro
                    else:
                        x0 = xcentro
                        xant = fcentro
                    temp = xcentro
                    xcentro = x0 - (xant*(x1-x0)/(xact-xant))
                    fcentro = f(xcentro)
                    err = abs(xcentro - temp)
                    cont += 1
                    #print(cont, "|", x0,"|",x1,"|",xcentro,"|",fcentro,"|",err)
                    print(cont, "|",xcentro,"|",fcentro,"|",err)
                if (fcentro == 0):
                    print(xcentro,"es raiz")
                else:
                    if(err < tol):
                        print('\n')
                        print(xcentro,"es una aproximacion a la raiz")
                        print(err, "con error")
                    else:
                        print("el metodo fracaso")
            else:
                print("el intervalo no sirve")

def f(x):
    return exp(-x+1) - x**2 + 4*x + (7*(cos(x**2 - 4)**2)) -7


regla_falsa()