'''- Implementar el Metodo Clasico de Ringe-Kuta de orden 4 para resolver la ecuacion diferencial

.x'(t) = f(t, x(t))
.x(t0) = x0

para una funcion f(t, x) cualquiera.

- Para la siguiente ecuaci´on diferencial

.x'(t) = t−2(tx(t) − x(t)2)
.x(1) = 2 

Resolver usando el metodo clasico de Runge Kuta de orden 4, con paso h = 0.005 , en el intervalo
[1, 3]. Graficar la solucion usando Splines Cubicos.

'''

import matplotlib.pyplot as plt
import numpy as np


def runge_kuta_orden_4(h, pasos, x0, t0, f):
    x = x0
    t = t0
    X = [x]
    T = [t]
    for i in range(pasos):
        F1 = h * f(t, x)
        F2 = h * f(t + 1 / 2 * h, x + 1 / 2 * F1)
        F3 = h * f(t + 1 / 2 * h, x + 1 / 2 * F2)
        F4 = h * f(t + h, x + F3)
        x = x + 1 / 6 * (F1 + 2 * F2 + 2 * F3 + F4)
        t = t + h
        T.append(t)
        X.append(x)
    return T, X


def graficar(T, X):
    plt.plot(T, X)
    plt.grid()
    plt.show()


def f(t, x):
    return (1 / np.power(t, 2)) * (t * x - np.power(x, 2))


def main():
    t0 = 1
    x0 = 2
    t_final = 3
    h = 0.005
    pasos = int(np.ceil((t_final - t0) / h))
    T, X = runge_kuta_orden_4(h, pasos, x0, t0, f)
    graficar(T, X)


main()
