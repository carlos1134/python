#ambos arrays tienen la misma longitud
#SEAN:
x = [2.718281828, -3.141592654, 1.414213562, 0.5772156649, 0.3010299957]
y = [1486.2497, 878366.9879, -22.37429, 4773714.647, 0.000185049]

'''Calcular serie(i=1 a n) [xiyi]  de la siguientes maneras
(a) para adelante : serie(i=1 a n) [xiyi]
(b) para atras : serie(i=n a 1) [xiyi]
(c) positivos de mayor a menor + negativos de menor a mayor
(d) positivos de menor a mayor + negativos de mayor a menor
Cual resultado es mas confiable y por que?'''

def problema_a():
    suma = 0
    for i in range(len(x)):
        producto = x[i]*y[i]
        print('Resultado parcial: {} + {}'.format(suma, producto))
        suma += producto
    return suma


def problema_b():
    suma = 0
    for i in reversed(range(len(x))):
        producto = x[i]*y[i]
        print('Resultado parcial: {} + {}'.format(suma, producto))
        suma += producto
    return suma


def ordenar_terminos_suma():
    productos_positivos = []
    productos_negativos = []
    for i in range(len(x)):
        producto = x[i]*y[i]
        if producto >= 0:
            productos_positivos.append(producto)
        else:
            productos_negativos.append(producto)
    return productos_positivos, productos_negativos


def problema_c():
    productos = ordenar_terminos_suma()
    productos_positivos_de_mayor_a_menor = sorted(productos[0], reverse=True)
    productos_negativos_de_menor_a_mayor = sorted(productos[1])
    suma_positivos = sumar(productos_positivos_de_mayor_a_menor)
    suma_negativos = sumar(productos_negativos_de_menor_a_mayor)
    print('Suma positivos de mayor a menor: ', suma_positivos)
    print('Suma negativos de menor a mayor: ', suma_negativos)
    return suma_positivos + suma_negativos


def problema_d():
    productos = ordenar_terminos_suma()
    productos_negativos_de_mayor_a_menor = sorted(productos[0])
    productos_positivos_de_menor_a_mayor = sorted(productos[1], reverse=True)
    suma_positivos = sumar(productos_positivos_de_menor_a_mayor)
    suma_negativos = sumar(productos_negativos_de_mayor_a_menor)
    print('Suma positivos de menor a mayor: ', suma_positivos)
    print('Suma negativos de mayor a menor: ', suma_negativos)
    return suma_positivos + suma_negativos


def sumar(array):
    '''Suma los elementos de un array mostrando cada par de numeros a sumar, de manera que se pueda visualizar si
    alguna de estas operaciones puede restar numeros parecidos'''
    suma = 0
    for numero in array:
        print("Resultado parcial: {} + {}".format(suma, numero))
        suma += numero
    return suma


if __name__ == '__main__':
    '''Conclusiones
    El mas confiable es el d. 
    Por empezar, que esten ordenados le da mas confiabilidad a que no lo esten porque hay menos riesgo de sumar números 
    muy grandes con otros muy chicos. 
    A su vez, dentro de los que están ordenados, conviene sumar los positivos de menor
    a mayor, porque el resultado parcial en cada paso va haciendo que el numero vaya creciendo, 
    se hace mas significativo y vuelve a reducir el riesgo de sumar cosas muy diferentes. Lo miso aplica para los 
    negativos de mayor a menor.
    '''

    print('Ejercicio a')
    print('Resultado final: ', problema_a())
    print('-------------')

    print('Ejercicio b')
    print('Resultado final: ', problema_b())
    print('-------------')

    print('Ejercicio c')
    print('Resultado final: ', problema_c())
    print('-------------')

    print('Ejercicio d')
    print('Resultado final: ', problema_d())

