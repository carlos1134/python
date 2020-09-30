'''. Escribir un algoritmo para resolver la ecuacion del calor con condiciones de borde homogeneas
(igual a 0) usando el metodo implıcito (usando backward difference para discretizar la derivada
primera). Usar este algoritmo para encontrar una soluci´on aproximada de la siguiente ecuacion
diferencial

.uxx = ut, t ≥ 0, x ∈ [0, 1]
.u(x, 0) = sin(πx), x ∈ [0, 1]
.u(0, t) = u(1, t) = 0, t ≥ 0

Graficar la solucion u.

'''

import numpy as np
import scipy.sparse.linalg as sp
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.sparse import diags


def construir_matriz_tridiagonal(s, n):
    diagonales = [[-s]*(n-1), [1+2*s]*n, [-s]*(n-1)]
    return diags(diagonales, [-1, 0, 1], format='csr')


def resolver_ecuacion_diferencial_metodo_implicito(s, pasos, U0):
    U0 = np.concatenate(([0], U0))
    U0 = np.concatenate((U0, [0]))
    solucion = [U0]

    matriz = construir_matriz_tridiagonal(s, pasos)

    for i in range(1, pasos):
        U_actual = solucion[i - 1][1:-1]
        U_siguiente = sp.spsolve(matriz, U_actual)
        U_siguiente = np.concatenate(([0], U_siguiente))
        U_siguiente = np.concatenate((U_siguiente, [0]))
        solucion.append(U_siguiente)

    return np.array(solucion)


def graficar_solucion(solucion, t_final):
    x = np.linspace(0, 1, len(solucion[0]))
    t = np.linspace(0, t_final, len(solucion))
    x_mesh, t_mesh = np.meshgrid(x, t)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    sup = ax.plot_surface(x_mesh, t_mesh, solucion, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(sup)

    plt.show()


def main():
    t_final = 1
    h = 0.01
    k = 0.01
    s = k / np.power(h, 2)
    pasos = int(t_final / k)
    x = np.linspace(0, 1, int(1/h))
    U0 = np.sin(np.pi*x)
    solucion = resolver_ecuacion_diferencial_metodo_implicito(s, pasos, U0)
    graficar_solucion(solucion, t_final)


main()

