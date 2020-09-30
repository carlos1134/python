import math
import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace

gr = (math.sqrt(5) + 1) / 2
x = randint(10)

def f(x):
    return (x-3)**2

a = 0
b = 6

def gss(f, a, b, tol=1e-8):
    
    i = 0
    u = (b - a) / gr
    #dos puntos en x dentro del intervalo [a,b] de la funcion f 
    c = b - u   
    d = a + u
 
    while abs(c - d) > tol:
        print('------------------------')
        if f(c) < f(d):
            b = d
            xopt = b
        else:
            a = c
            xopt = a

        # Volvemos a calcular tanto c como d aquí para evitar la pérdida de precisión
        #que puede conducir a resultados incorrectos o bucle infinito
        i += 1
        u = (b - a) / gr
        c = b - u
        d = a + u
        print('iteración ', str(i+1))
        print ('xopt:', round(xopt, 6))
    plt.plot(xopt , f(xopt), color='red', marker='o') # marcamos con un punto rojo en la grafica el xopt final
    return (b + a) / 2

gss(f, a, b, tol=1e-8) #ejecuto el metodo gss

#grafico f
X = linspace(a,b,100)
Y = linspace(0,10,100)
plt.plot(X, [f(i) for i in X])
plt.xlabel('x')
plt.ylabel('y')

plt.show()
