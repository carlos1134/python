'''Para la siguiente ecuacion diferencial:

.x'(t) = cos(t) − sin(x(t)) + t^2
.x(−1) = 3 

Resolver usando el metodo de Taylor de orden 4, con paso h = 0.01 , usar 200 puntos. Graficar
la solucion usando Splines Cubicos.'''

import numpy as np
import matplotlib.pyplot as plt
import math


def metodo_taylor_orden_n(h, pasos, t0, x0, funciones_derivadas, orden):
    t = t0
    x = x0
    T = [t]
    X = [x]
    for i in range(pasos):
        derivadas_evaluadas = [funciones_derivadas[0](t, x)]
        for k in range(1, orden):
            derivadas_evaluadas.append(funciones_derivadas[k](t, x, derivadas_evaluadas))
        for j in range(orden):
            x = x + derivadas_evaluadas[j] * np.power(h, j + 1) / math.factorial(j + 1)
        t = t + h
        T.append(t)
        X.append(x)
    return T, X


def x_prima(t, x):
    return np.cos(t) - np.sin(x) + np.power(t, 2)


def x_segunda(t, x, derivadas_dependientes):
    x_prima = derivadas_dependientes[0]
    return -np.sin(t) - x_prima * np.cos(x) + 2 * t


def x_tercera(t, x, derivadas_dependientes):
    x_prima = derivadas_dependientes[0]
    x_segunda = derivadas_dependientes[1]
    return -np.cos(t) - x_segunda * np.cos(x) + np.power(x_prima, 2) * np.sin(x) + 2


def x_cuarta(t, x, derivadas_dependientes):
    x_prima = derivadas_dependientes[0]
    x_segunda = derivadas_dependientes[1]
    x_tercera = derivadas_dependientes[2]
    return np.sin(t) + (np.power(x_prima, 3) - x_tercera) * np.cos(x) + 3 * x_prima * x_segunda * np.sin(x)


def graficar(T, X):
    plt.plot(T, X)
    plt.grid()
    plt.show()


def main():
    t0 = -1
    x0 = 3
    pasos = 200
    h = 0.01
    derivadas = [x_prima, x_segunda, x_tercera, x_cuarta]
    T, X = metodo_taylor_orden_n(h, pasos, t0, x0, derivadas, 4)
    graficar(T, X)


main()
