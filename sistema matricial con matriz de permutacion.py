'''Escribir un codigo para resolver el sistema matricial Ax = b donde A es una matriz que es una
permutacion de una matriz triangular superior.'''


def resolver_sistema(matriz_coeficientes, b, p):
    x = [None]*len(matriz_coeficientes)
    for i in reversed(range(len(matriz_coeficientes))):
        suma = 0
        for j in range(i+1, len(matriz_coeficientes)):
            suma += matriz_coeficientes[p[i]][j] * x[j]
        x[i] = (b[p[i]] - suma) / matriz_coeficientes[p[i]][i]

    return x


if __name__ == '__main__':
    A = [
        [0, 2, -1],
        [0, 0, 2],
        [2, 1, -1]
    ]
    b = [4, 2, 5]
    p = [2, 0, 1]
    print(resolver_sistema(A, b, p))
