'''Escribir un codigo para estimar la norma infinito de una matriz, usar la formula cerrada. C´omo
serıa un codigo si no tenemos una formula cerrada? Comparar'''

import numpy as np
import random


def calcular_norma_infinito(matriz):
    sumas_filas = []
    for fila in matriz:
        suma = 0
        for numero in fila:
            suma += abs(numero)
        sumas_filas.append(suma)
    return max(sumas_filas)


def estimar_norma_infinito(matriz):
    max = 0
    longitud_vector = len(matriz[0])
    for i in range(1, 10**4):
        x = generar_x_unitario_aletorio(longitud_vector)
        s = np.linalg.norm(np.matmul(matriz, x), ord=np.inf)
        if s > max:
            max = s
    return max


def generar_x_unitario_aletorio(longitud):
    y = [random.uniform(-1, 1) for num in range(longitud)]
    x = [yi/np.linalg.norm(y, ord=np.inf) for yi in y]
    return x


if __name__ == '__main__':
    matriz = [[7, -4], [-5, 8]]
    print(calcular_norma_infinito(matriz))
    print(estimar_norma_infinito(matriz))

'''en la estimacion, a mayor rango, mayor acercamiento al resultado'''
