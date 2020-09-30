''' Considerar la sucesion x0 = 1, x1 = 1/3, xn+1 = (13/3)xn −(4/3)x(n−1)

Dar una formula cerrada para xn. Escribir un programa que calcule xn de ambas formas y comparar.
Cual es mas confiable?'''


import math


def x(n):
    '''Calcula termino xn de la sucesion de forma recursiva'''
    if n == 0:
        return 1.0
    elif n == 1:
        return 1/3
    else:
        return (13/3)*x(n-1)-(4/3)*x(n-2)


def x_forma_cerrada(n):
    '''Calcula termino xn de la sucesion con la formula cerrada'''
    return math.pow(1/3, n)

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
        print('Termino ',(i))
        print('Forma recursiva: ',(salida_recursiva[i]))
        print('Forma cerrada: ',(salida_cerrada[i]))
        print('Error: ',(errores[i]))
        print('\n')

if __name__ == '__main__':
    salida = comparar_calculos(33, x, x_forma_cerrada)
    mostrar_comparaciones(salida[0], salida[1], salida[2])
    '''Se observa que para terminos mas elevados, el error es cada vez mas grande, al punto que a partir
    del termino 29 supera la unidad. La forma mas confiable es usando la formula cerrada, ya que cuanto mayor es n en
    la forma recursiva, cada vez resto numeros mas parecidos. Además de esta forma estoy amplificando el error al
    multiplicar los Xi por numeros mayores a 1, y tambien arrastro los errores en el término siguiente.'''
