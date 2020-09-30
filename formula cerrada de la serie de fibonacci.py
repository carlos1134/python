'''Consideremos la siguiente modificacion de la serie de Fibonacci :

r0 = 1          r1 = [1 − (5)^0.5]/2          r(n+1) = rn + r(n−1)

Cual es la formula cerrada rn? Es la formula recursiva una manera estable de calcular rn ?'''


import math


def r(n):
    if n == 0:
        return 1
    elif n == 1:
        return (1-math.sqrt(5))/2
    else:
        return r(n-1)+r(n-2)


def r_forma_cerrada(n):
    return math.pow((1-math.sqrt(5))/2, n)

def comparar_calculos(cantidad_terminos, forma_recursiva, forma_cerrada):
    '''Dada una cantidad de terminos, devuelve una lista con los calculos de forma recursiva,
    una lista con los calculos con la formula cerrada, y otra de los errores en cada termino'''
    salida_recursiva = []
    salida_cerrada = []
    errores = []
    for i in range(cantidad_terminos):
        salida_recursiva.append(forma_recursiva(i))
        salida_cerrada.append(forma_cerrada(i))
        errores.append(abs(salida_cerrada[i] - salida_recursiva[i]))
    return salida_recursiva, salida_cerrada, errores


def mostrar_comparaciones(salida_recursiva, salida_cerrada, errores):
    '''Muestra por pantalla la salida de comparar_calculos'''
    for i in range(len(salida_recursiva)):
        print('Termino {}'.format(i))
        print('Forma recursiva: {}'.format(salida_recursiva[i]))
        print('Forma cerrada: {}'.format(salida_cerrada[i]))
        print('Error: {}'.format(errores[i]))
        print('\n')


if __name__ == '__main__':
    salida = comparar_calculos(32, r, r_forma_cerrada)
    mostrar_comparaciones(salida[0], salida[1], salida[2])



    '''Si bien la formula cerrada es mas confiable que la recursiva porque no arrastra errores de terminos anteriores,
    a diferencia del ejercicio 9 el error no crece de manera tan grande; no se restan numeros parecidos, ni se
    multiplica a algun Xi por un numero mayor o igual a 1. Por eso, se puede decir que la forma recursiva en este caso
    es una manera estable de resolver el problema'''
