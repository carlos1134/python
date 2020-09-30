'''Sea
    yn = integral(0 a 1) [x^n * e^x dx]
    
Integrar por partes para obtener una formula recurrente para yn. Mostrar que limn→∞yn = 0 .
Hacer un programa para calcular los primeros 30 terminos de yn.'''



import math


def f(x, n):
    return math.pow(x, n)*math.pow(math.e, x)


def y(n):
    '''Calcula yn de forma recursiva'''
    if n == 0:
        return math.e - 1
    else:
        return math.e - n*y(n-1)


def calcular_primeros_n_terminos(n):
    for i in range(n):
        print('Termino {}: {}'.format(i, y(i)))


if __name__ == '__main__':
    calcular_primeros_n_terminos(30)
    '''Del resultado teorico sabemos que a medida que n crece, yn tiende a cero. Sin embargo, en el calculo
     vemos que si bien en los primeros terminos esto es cierto, a partir del termino 18 se observan valores 
     alternantes positivos y negativos que crecen cada vez mas. Esto es porque el n amplifica el error, y en cada
     termino se va acumulando el error del paso anterior'''
