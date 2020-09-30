'''Escribir un programa para calcular

f(x) = ((x^2 + 1)^0.5) − 1

g(x) = x^2/[((x^2 + 1)^0.5) + 1]

para la sucesion 8^−1, 8^−2, 8^−3. . . , 8^−10.
Aunque f = g la computadora produce resultados distintos,cual es m´as confiable?
'''


import math


def f(x):
    return math.sqrt(math.pow(x, 2)+1)-1


def g(x):
    return (math.pow(x, 2))/(math.sqrt(math.pow(x, 2)+1)+1)


def evaluar_sucesion_en_ambas_funciones():
    numero = 8
    salida_f = []
    salida_g = []
    errores = []
    for i in range(1, 8):
        salida_f.append(f(math.pow(numero, -i)))
        salida_g.append(g(math.pow(numero, -i)))
        errores.append(abs(salida_f[i-1]-salida_g[i-1]))
    return salida_f, salida_g, errores


def mostrar_comparaciones(salida_f, salida_g, errores):
    for i in range(len(salida_f)):
        print('Termino',(i+1))
        print('Salida con f:', (salida_f[i]))
        print('Salida con g:',(salida_g[i]))
        print('Error: ', (errores[i]))
        print('\n')


if __name__ == '__main__':
    salida = evaluar_sucesion_en_ambas_funciones()
    mostrar_comparaciones(salida[0], salida[1], salida[2])
    '''Para la suce4sion 8^-1, ... 8^⁻10, a medida que crece el n, el termino se aproxima mas a cero, y la raiz se
    aproxima mas a 1. En f, estoy restando numeros parecidos. En cambio, en g los estoy sumando.
    Es mas confiable el resultado que produce g'''
