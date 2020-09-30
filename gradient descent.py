import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace

# Ejemplo del gradiente descendente aplicado a la función y = x^2 + 1

x_inicial = randint(10)
alpha = 0.1
n_iteraciones = 15
h = 0.000001
e = 0.001
error = 100
iteraciones = []
y = []
x = x_inicial
i=0

def fun (x):
    return x**2 + 1    

def grad (x):
    return  (fun(x+h)-fun(x-h))/(2*h)


while (error > e):
    print('------------------------')
    print('iteración ', i)
    # Calcular gradiente
    gradiente = grad(x)

    # Actualizar "x" usando gradiente descendente
    xopt = x - alpha*gradiente

    y.append(fun(xopt))
    iteraciones.append(i+1)

    # Imprimir resultados
    error = abs(xopt - x)
    print('x = ', str(xopt), ', y = ', fun(x))
    x = xopt
    i += 1
    if(error < e):
        x1 = plt.subplot(1,2,2)
        x1.plot(xopt , fun(xopt), color='red', marker='o')  # marco en la funcion con un punto rojo el xopt final

#mostraremos la cantidad de iteraciones tambien
plt.subplot(1,2,1)
plt.plot(iteraciones,y)
plt.xlabel('Iteración')
plt.ylabel('y')


#funcion fun
X = linspace(-5,5,100)
Y = fun(x)
x1.plot(X,[fun(i) for i in X])
plt.xlabel('x')
plt.ylabel('y')

plt.show()

