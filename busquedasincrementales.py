def f(fun, x):
    y = eval(fun)
    return y
  
def busquedasincrementales():
  
    fun = input("ingresa tu función")
    a = float(input("ingresa el límite inferior del intervalo"))
    b = float(input("ingresa el límite superior del intervalo"))
    delta = float(input("ingresa el delta"))
    iteraciones = int(input("ingrese el número máximo de iteraciones"))
  
    i = 1
    while(f(fun, a)*f(fun, b) > 0 and i <= iteraciones):
      a = b
      b = a + delta
      i = i + 1
      
    if f(fun, a)*f(fun, b) < 0:
        print("Hay raíz entre ", a, " y ", b)
        
    if i > iteraciones:
        print("Se superó el límite de iteraciones")
 
busquedasincrementales()
