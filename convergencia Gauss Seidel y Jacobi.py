''' Para el siguiente sistema (en el main) mostrar que tanto Gauss Seidel como Jacobi convergen
para cualquier valor inicial. Usar el ´ıtem anterior para estimar la solucion'''

from copy import deepcopy
import random

def algoritmo_jacobi(matriz, b, pasos, x_inicial):
    matriz_aux = deepcopy(matriz)
    b_aux = deepcopy(b)
    vector_resultado = deepcopy(x_inicial)
    u = [None]*len(matriz)
    anticipar_divisiones(b_aux, matriz_aux)
    for k in range(pasos):
        for l in range(len(matriz_aux)):
            u[l] = b_aux[l] - suma(matriz_aux, vector_resultado, l)
        for m in range(len(matriz)):
            vector_resultado[m] = u[m]
    return vector_resultado

def algoritmo_gauss_seidel(matriz, b, pasos, x_inicial):
    matriz_aux = deepcopy(matriz)
    b_aux = deepcopy(b)
    vector_resultado = deepcopy(x_inicial)
    anticipar_divisiones(b_aux, matriz_aux)
    for k in range(pasos):
        for i in range(len(matriz)):
            vector_resultado[i] = b_aux[i] - suma(matriz_aux, vector_resultado, i)
    return vector_resultado

def anticipar_divisiones(b_aux, matriz_aux):
    for i in range(len(matriz_aux)):
        d = 1 / matriz_aux[i][i]
        b_aux[i] *= d
        for j in range(len(matriz_aux)):
            matriz_aux[i][j] *= d


def suma(matriz, x, indice):
    salida = 0
    for j in range(len(matriz)):
        if indice != j:
            salida += matriz[indice][j]*x[j]
    return salida

if __name__ == '__main__':
    A = [
        [2, -1, 0],
        [1, 6, -2],
        [4, -3, 8]
    ]
    b = [2, -4, 5]
    x0 = [random.randrange(0, 999999999999) for i in range(len(A))]
    for i in range(3):
        print('x inicial: ', x0)
        print('Resultado Gauss-Seidel: ', algoritmo_gauss_seidel(A, b, 1000, x0))
        print('Resultado Jacobi: ', algoritmo_jacobi(A, b, 1000, x0))
        print()
