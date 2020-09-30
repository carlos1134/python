'''dada Ax = b - Usar el proceso de eleminacion de Gauss Escalado para encontrar la descomposicion
PA=LU  y resolver en cada uno de los casos.'''

from copy import deepcopy
import numpy.linalg as linalg

def calcular_vector_s(matriz):
    s = []
    for fila in matriz:
        v_abs = [abs(x) for x in fila]
        s.append(max(v_abs))
    return s


def obtener_pivote(matriz, p, s, k):
    indice_max = k
    valor_max = abs(matriz[p[k]][k])/s[p[k]]
    for j in range(k, len(matriz)):
        candidato_max = abs(matriz[p[j]][k])/s[p[j]]
        if candidato_max > valor_max:
            valor_max = candidato_max
            indice_max = j
    return indice_max


def intercambiar(vector, indice1, indice2):
    v = deepcopy(vector)
    temp = v[indice1]
    v[indice1] = v[indice2]
    v[indice2] = temp
    return v


def eliminacion_de_gauss_escalado(matriz_original):
    matriz = deepcopy(matriz_original)
    p = [x for x in range(len(matriz))]
    s = calcular_vector_s(matriz)
    for k in range(len(matriz)):
        j = obtener_pivote(matriz, p, s, k)
        p = intercambiar(p, j, k)
        for i in range(k+1, len(matriz)):
            z = matriz[p[i]][k] / matriz[p[k]][k]
            matriz[p[i]][k] = z
            for l in range(k+1, len(matriz)):
                matriz[p[i]][l] -= z * matriz[p[k]][l]
    return matriz, p


def obtener_solucion(matriz, b_original, p):
    b = deepcopy(b_original)
    vector_resultado = [None]*len(matriz)
    for k in range(len(matriz)-1):
        for i in range(k+1, len(matriz)):
            b[p[i]] -= matriz[p[i]][k]*b[p[k]]
    for i in reversed(range(0, len(matriz))):
        suma = 0
        for j in range(i+1, len(matriz)):
            suma += matriz[p[i]][j] * vector_resultado[j]
        vector_resultado[i] = (b[p[i]] - suma)/matriz[p[i]][i]
    return vector_resultado


if __name__ == '__main__':
    A1 = [
        [-1, 1, -4],
        [2, 2, 0],
        [3, 3, 2]
    ]
    b1 = [0, 1, 1/2]
    matriz1, p1 = eliminacion_de_gauss_escalado(A1)
    resultado1 = obtener_solucion(matriz1, b1, p1)
    resultado_np_1 = linalg.solve(A1, b1)
    print('Sistema 1')
    print('Resultado algoritmo implementado: ', resultado1)
    print('Resultado algoritmo de numpy.linalg: ', resultado_np_1)
    print('--------')
    A2 = [
        [1, 6, 0],
        [2, 1, 0],
        [0, 2, 1]
    ]
    b2 = [3, 1, 1]
    matriz2, p2 = eliminacion_de_gauss_escalado(A2)
    resultado2 = obtener_solucion(matriz2, b2, p2)
    resultado_np_2 = linalg.solve(A2, b2)
    print('Sistema 2')
    print('Resultado algoritmo implementado: ', resultado2)
    print('Resultado algoritmo de numpy.linalg ', resultado_np_2)
