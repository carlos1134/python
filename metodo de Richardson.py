''' Calcular el sistema dado en el main con el metodo de Richardson '''

from copy import deepcopy


def metodo_richardson(matriz, b, pasos, x_inicial):
    resultado = deepcopy(x_inicial)
    for k in range(pasos):
        for i in range(len(matriz)):
            resultado[i] = (resultado[i] - suma(matriz, resultado, i)) + b[i]
    return resultado


def suma(matriz, x, indice):
    salida = 0
    for j in range(len(matriz)):
        salida += matriz[indice][j] * x[j]
    return salida


if __name__ == '__main__':
    A = [
        [1, 1/2, 1/3],
        [1/3, 1, 1/2],
        [1/2, 1/3, 1]
    ]
    b = [11/18, 11/18, 11/18]
    print(metodo_richardson(A, b, 100, [1, 1, 1]))
