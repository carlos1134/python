''' .Un modelo de probabilidades de default: Extended CreditGrades Model with Stochastic
Volatility and Jumps
Implementar el modelo Double-Exponential Jump Difusion para calcular precios de una call y probabilidades de
default, para simplificar tomar t = 0.
Para encontrar las raıces usar diferentes tolerancias (rtol) y los siguiente algoritmos de root finding:
• scipy.optimize.brentq
• scipy.optimize.bisect
• usando el algorirmo del item 1
En todos los casos calcular el tiempo que tarda el algoritmo para llegar a la ra´ız deseada.
Para cada algoritmo y tolerancia decidir si el modelo es confiable.
Con que root finding y rtol conviene implementar el algoritmo?
. Usar el modelo del item anterior para estimar precios de call y probabilidades de default de General
Motors (usar los par´ametros de la pg. 20). Graficar los precios de call y las probabilidades de default
en funcion del tiempo (T).'''

import scipy.optimize
import numpy.linalg.linalg as linalg
import numpy as np
import time
import matplotlib.pyplot as plt
from numero_de_coeficientes import coeficientes
from ejercicio1 import newton_raphson_biseccion


class Dejd:

    def __init__(self, n_mas, n_menos, q_mas, lamb, k_nu, nu_inf, nu_0, funcion_busqueda_raices, tolerancia):
        self.R = 0.5
        self.n_mas = n_mas
        self.n_menos = n_menos
        self.q_mas = q_mas
        self.q_menos = 1 - q_mas
        self.lamb = lamb
        self.k_nu = k_nu
        self.nu_inf = nu_inf
        self.nu_0 = nu_0
        self.p = 0
        self.funcion_busqueda_raices = funcion_busqueda_raices
        self.tolerancia = tolerancia

#para que el init no sea tan engorroso con tantos parametros juntos, pongo una funcion agregando los parametros restantes
    def agregar_mas_parametros(self, S0, T0, d, D0, r=0.03):
        self.S0 = S0
        self.T0 = T0
        self.d = d
        self.D0 = D0
        self.r = r

    def precio_call(self, k, t):
        print('T = {}'.format(t))
        print('')
        return (self.D(t) + k) * np.exp(-self.r * t) * self.v(self.tau(t), self.y(k, t), k, t)

    def probabilidad_supervivencia(self, t):
        print('T = {}'.format(t))
        print('')
        return self.v_probabilidad_supervivencia(self.tau(t), self.y(0, t))

    def v(self, tau, y, k, t):
        suma = 0
        for j in range(1, 15):
            print('Iteracion {}'.format(j))
            p = j * (np.log(2) / tau)
            u =  self.u(p, y, k, t)
            suma += coeficientes[j - 1] * u
        return (np.log(2) / tau) * suma

    def v_probabilidad_supervivencia(self, tau, y):
        suma = 0
        for j in range(1, 15):
            print('Iteracion {}'.format(j))
            p = j * (np.log(2) / tau)
            u = self.u_probabilidad_supervivencia(p, y)
            suma += coeficientes[j - 1] * u
        return (np.log(2) / tau) * suma

    def coeficientes_polinomio(self, p):
        B4 = (1 / 2) * self.n_menos * self.n_mas
        B3 = (self.mu() * self.n_menos * self.n_mas) - (1 / 2) * (self.n_menos - self.n_mas)
        B2 = -((1 / 2) + self.mu() * (self.n_menos - self.n_mas) + (p + self.lamb) * self.n_menos * self.n_mas)
        B1 = -self.mu() + (p + self.lamb) * (self.n_menos - self.n_mas) - self.lamb * (
                self.q_mas * self.n_menos - self.q_menos * self.n_mas)
        B0 = p

        return B4, B3, B2, B1, B0

    def polinomio(self, x, p):
        B4, B3, B2, B1, B0 = self.coeficientes_polinomio(p)

        return B4 * np.power(x, 4) + B3 * np.power(x, 3) + B2 * np.power(x, 2) + B1 * x + B0

    def polinomio_derivado(self, x, p):
        B4, B3, B2, B1, B0 = self.coeficientes_polinomio(p)
        return 4 * B4 * (x ** 3) + 3 * B3 * (x ** 2) + 2 * B2 * x + B1

    def calcular_raices(self, p):
        raices = []
        intervalos = [[-100, -1 / self.n_menos], [-1 / self.n_menos, 0], [0, 1 / self.n_mas], [1 / self.n_mas, 100]]
        for num_intervalo, intervalo in enumerate(intervalos):
            if num_intervalo == 0 or num_intervalo == (len(intervalos) - 1):
                self.redimensionar_intervalo(intervalo, p, num_intervalo)
            t1 = time.time()
            raiz_bisect = scipy.optimize.bisect(self.polinomio, intervalo[0], intervalo[1], args=(p,), maxiter=1000, rtol=self.tolerancia)
            t2 = time.time()
            duracion_bisect = t2 - t1
            t1 = time.time()
            raiz_brentq = scipy.optimize.brentq(self.polinomio, intervalo[0], intervalo[1], args=(p,), maxiter=1000, rtol=self.tolerancia)
            t2 = time.time()
            duracion_brentq = t2 - t1
            t1 = time.time()
            raiz_nrb = newton_raphson_biseccion(self.polinomio, self.polinomio_derivado, intervalo[0], intervalo[1], args=(p,), maxiter=1000, rtol=self.tolerancia)
            t2 = time.time()
            duracion_nrb = t2 - t1
            print('Intervalo', 3 - num_intervalo)
            print('Duracion bisect: ', duracion_bisect)
            print('Duracion brent: ', duracion_brentq)
            print('Duracion newton-r b', duracion_nrb)
            raices.append(raiz_brentq)   # Cambiar por raiz_nrb o raiz_bisect para que calcule con los otros algoritmos
        raices.reverse()  # para que la salida sea fi0, fi1, fi2, fi3
        return raices

    def redimensionar_intervalo(self, intervalo, p, num_intervalo):
        while self.polinomio(intervalo[0], p) * self.polinomio(intervalo[1], p) >= 0:
            if num_intervalo == 0:
                intervalo[1] = intervalo[0]
                intervalo[0] *= 10
            else:
                intervalo[0] = intervalo[1]
                intervalo[1] *= 10

    def generar_sistema_ecuaciones(self, raices, p):
        matriz_coeficientes = [
            [1, 1, -1, -1],
            [raices[0], raices[1], -raices[2], -raices[3]],
            [1 / (raices[0] * self.n_menos + 1), 1 / (raices[1] * self.n_menos + 1),
             -1 / (raices[2] * self.n_menos + 1),
             -1 / (raices[3] * self.n_menos + 1)],
            [1 / (raices[0] * self.n_mas - 1), 1 / (raices[1] * self.n_mas - 1), -1 / (raices[2] * self.n_mas - 1),
             -1 / (raices[3] * self.n_mas - 1)]
        ]
        print('Numero de condicion de matriz: ', linalg.cond(matriz_coeficientes))
        print('')
        vector_resultado = [0, 1 / p, (1 / (p * (self.n_menos + 1))) - (1 / p), (1 / (p * (self.n_mas - 1))) + (1 / p)]

        return matriz_coeficientes, vector_resultado

    def resolver_sistema(self, raices, p):
        matriz_coeficientes, vector_resultado = self.generar_sistema_ecuaciones(raices, p)
        c0, c1, c2, c3 = linalg.solve(matriz_coeficientes, vector_resultado)

        return c0, c1, c2, c3

    def generar_coeficientes_u(self, raices, sol_sistema, k, t):
        b = - self.a(k, t)
        a2_mas = ((1 + raices[2] * self.n_menos) / (raices[3] - raices[2])) * (
                ((raices[0] - raices[3]) * sol_sistema[0] * np.exp((raices[0] - raices[2]) * b)) /
                (raices[0] * self.n_menos + 1) +
                ((raices[1] - raices[3]) * sol_sistema[1] * np.exp((raices[1] - raices[2]) * b)) /
                (raices[1] * self.n_menos + 1))
        a3_mas = ((1 + raices[3] * self.n_menos) / (raices[3] - raices[2])) * (
                ((raices[0] - raices[2]) * sol_sistema[0] * np.exp((raices[0] - raices[3]) * b)) /
                (raices[0] * self.n_menos + 1) +
                ((raices[1] - raices[2]) * sol_sistema[1] * np.exp((raices[1] - raices[3]) * b)) /
                (raices[1] * self.n_menos + 1))
        a3_menos = - a3_mas
        return a2_mas, a3_menos

    def u(self, p, y, k, t):
        raices = self.calcular_raices(p)
        c0, c1, c2, c3 = self.resolver_sistema(raices, p)
        a2_mas, a3_menos = self.generar_coeficientes_u(raices, [c0, c1, c2, c3], k, t)
        if y <= 0:
            return c0 * np.exp(raices[0] * y) + c1 * np.exp(raices[1] * y) + a2_mas * np.exp(raices[2] * y) + \
                   a3_menos * np.exp(raices[3] * y)
        else:
            return c2 * np.exp(raices[2] * y) + c3 * np.exp(raices[3] * y) + a2_mas * np.exp(raices[2] * y) + \
                   a3_menos * np.exp(raices[3] * y) + ((np.exp(y) / p) - (1 / p))

    def calclar_coeficientes_u_probabilidad_default(self, p, raices):
        a2 = -1 / p * ((raices[3] * (1 + self.n_menos * raices[2])) / (raices[3] - raices[2]))
        a3 = 1 / p * ((raices[2] * (1 + self.n_menos * raices[3])) / (raices[3] - raices[2]))
        return a2, a3

    def u_probabilidad_supervivencia(self, p, y):
        raices = self.calcular_raices(p)
        a2, a3 = self.calclar_coeficientes_u_probabilidad_default(p, raices)
        return a2 * np.exp(raices[2] * y) + a3 * np.exp(raices[3] * y) + 1 / p

    def alfa(self):
        return (self.q_mas / (1 - self.n_mas)) + (self.q_menos / (1 + self.n_menos)) - 1

    def mu(self):
        return -(1 / 2) - (self.lamb * self.alfa())

    def a(self, k, t):
        return np.log((self.D(t) + k) / self.D(t))

    def x(self):
        return np.log((self.S0 + self.D0) / self.D0)

    def y(self, k, t):
        return self.x() - self.a(k, t)

    def D(self, t):
        return self.D0 * np.exp((self.r - self.d) * t)

    def tau(self, t):
        return self.nu_inf * t - (((self.nu_0 - self.nu_inf) / self.k_nu) * (np.exp(-self.k_nu * t) - 1))


def main():
    gm = Dejd(0.0443, 0.1181, 0.4894, 162.5382, 1.2433, 0.0151, 0.0260, scipy.optimize.brentq, 1e-10)
    gm.agregar_mas_parametros(25.86, 0, 0.078, 32.5)

    tiempo = [t for t in range(1, 31)]
    print('PROBABILIDAD DE DEFAULT: ')
    print('')
    probabilidad_default = [1 - gm.probabilidad_supervivencia(t) for t in tiempo]
    print('_____________________________________________________________________________________')
    print('')
    print('PRECIO DE LA CALL')
    print('')
    precio_call = [gm.precio_call(30, t) for t in tiempo]

    _, ax = plt.subplots(1, 2)
    ax[0].plot(tiempo, precio_call)
    ax[0].set_ylabel('Precio call')
    ax[0].set_xlabel('Tiempo')
    ax[0].grid()
    ax[1].plot(tiempo, probabilidad_default)
    ax[1].set_ylabel('Probabilidad de default')
    ax[1].set_xlabel('Tiempo')
    ax[1].grid()
    plt.show()


if __name__ == '__main__':
    main()


'''
_____________________________________________________________________________________________________
ANALIZANDO LOS TIEMPOS PARA HALLAR LAS RAICES:

En casos generales, el algoritmo más rápido para el cálculo de raíces resulta ser brent.
Con respecto a bisección, y  newton-raphson combinado con bisección, los tiempos varían de tal forma que en algunas ocasiones uno se sitúa
levemente por encima de otro y se invierten los roles. Sabemos que bisección es un algoritmo lento porque no usa nada de información de la
función. Que el algoritmo de  Brent sea el que arroja menores tiempos se debe a que usa interpolación cuadrática inversa cada vez que puede,
y solo usa bisección en aquellos casos en los que se cae fuera del intervalo deseado. En cuanto a los algoritmos de bisección y Newton-Raphson
combinado con bisección, que los tiempos sean parecidos probablemente se deba a que, si bien el algoritmo combinado debería ser más
performante, fue implementado manualmente, mientras que bisección salió de las librerías de Scipy en las que seguramente se hacen muchas
optimizaciones para que corra de la manera más rápida posible. EN CONCLUSION: Puede haber casos en el que el algoritmo de biseccion y el
algoritmo de Newton-Raphson combinado con bisección sean mas performantes que el de brent; pero para funciones mas suaves, como en el que
vamos a observar, el algoritmo de Brent es casi siempre mas performante
_____________________________________________________________________________________________________
¿ A PARTIR DE CUANDO LAS CURVAS SE SUAVISAN?
    
ALGORITMO DE  BISECCION: Para tolerancias mayores o iguales a e^⁻8, los gráficos se vuelven inestables y oscilan mucho.
A partir de e^-9, las curvas se suavizan de tal forma que se puede observar mejor la tendencia.
    
ALGORITMO DE BRENT:     A partir de e^-8 las curvas se suavizan.
    
ALGORITMO DE NEWTON-RAPHSON:    A partir de e^-7 las curvas se suavizan.
    
Las curvas para cada algoritmo se mantienen aunque se incremente la cantidad de iteraciones. Lo que puede estar ocurriendo es que
entre dos iteraciones sucesivas, uno converja más rápido que los otros, de manera que el resultado final estará bastante por debajo de
la tolerancia, y nunca esté cortando por iteraciones.  
_____________________________________________________________________________________________________
ANALIZANDO LA CONFIABILIDAD:
Todos los algoritmos se corrieron variando las iteraciones máximas en 1000, 10000 y 100000 y se fue variando la tolerancia con
potencias inversas de e.
Otro problema de confiabilidad que se da tanto para probabilidad de default como para precio de la call es el del cálculo de la transformada
inversa de Laplace. Los resultados que arroja U son números pequeños menores a cero, mientras que algunos coeficientes que multiplican a la U
son números grandes que pueden amplificar cualquier error  en la representación.
_____________________________________________________________________________________________________
EN EL MODELO DEL PRECIO DE LA CALL, la función U depende de las raíces del polinomio, y de la solución del sistema de ecuaciones cuya matriz
depende también de las raíces del polinomio. Estas soluciones al sistema de ecuaciones son  muy poco confiables ya que el número de condición
de las matrices es mucho mayor que 1 en todos los casos. Oscila entre 20 y 120. Esto nos permite concluir que el modelo del precio de la call
no resulta ser confiable. (He mostrado por pantalla los numeros de condicion en cada iteraccion)

EN EL MODELO DE LA PROBABILIDAD DE DEFAULT, la funcion U depende de las raices del polinomio, y por el análisis hecho anteriormente,
eligiendo la tolerancia adecuada, podemos usar cualquiera de los algoritmos. Por una cuestión de performance, probablemente convenga
realizarlo con Brent, y una tolerancia menor a e^-8.

una vez terminado el tiempo T[1,31] se mostrara la grafica de los precios de call y las probabilidades de default
'''
