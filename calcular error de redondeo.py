'''- Si quiero calcular: serie(n=1 a inf) [xn]

con un error menor a e, dejo de sumar cuando |xn| < e ?. Ver con serie(n=1 a inf)[(0.99)^n]
Recordar que:

    serie(n=1 a inf) r^n = r/1−r si |r| < 1
'''

import math


def convergencia_serie(r):
    return r/(1-r)


def calcular_serie(epsilon):
    n = 1
    suma = math.pow(0.99, n)
    while abs(suma-convergencia_serie(0.99)) >= epsilon:
        n += 1
        potencia = math.pow(0.99, n)
        suma += potencia
        error_actual = abs(suma-convergencia_serie(0.99))
        if potencia < epsilon <= error_actual:
            print('Epsilon: {}, Error: {}, Valor calculado: {}'.format(epsilon, error_actual, potencia))


if __name__ == '__main__':
    epsilon = math.pow(10, -3)
    calcular_serie(epsilon)
    '''No es suficiente porque en un determinado momento (0.99)^n < epsilon, y sin embargo el error, modulo de
     suma - r/(1-r), sigue siendo mayor que epsilon. Cuando esto ocurre, se imprime por pantalla el epsilon, el error y
     el valor actual de la suma'''
