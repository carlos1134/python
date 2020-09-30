import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

fun = lambda th: np.sin( th[0]**2 + th[1]**2) #funcion
e = 0.0001
res = 100
error=1

_x = np.linspace(-3, 3, res)
_y = np.linspace(-3, 3, res)
_z = np.zeros((res, res))

for ix, x in enumerate(_x):
    for iy, y in enumerate(_y):
        _z[iy, ix] = fun([x, y])

plt.contourf(_x, _y, _z, 100)
plt.colorbar()                      #FORMADO LA GRAFICA

theta = np.random.rand(2)*4 - 2     #RAMDON THETA DE -2 a 2
_T = np.copy(theta)                 # COPIA 
h = 0.001
lr = 0.0001     #UN LR MAS GRANDE QUE ESTE LO QUE HARA ES DAR SALTOS POR TODA LA GRAFICA 

plt.plot(theta[0], theta[1], 'o', color ='white')


grad = np.zeros(2)
i=1
#for i in range(10000):     #ACA PODRIA ACTIVAR EL FOR COMENTANDO EL WHILE Y EL GENERADOR DE CORTE PARA QUE EL ALGORITMO CONTINUE
while (True):
    for it, th in enumerate(theta):
        _T[it] = _T[it] + h
        deriv = (fun(_T) - fun(theta))/h
        grad[it] = deriv
        thetaopt = theta - lr*grad
        error = np.sum(abs(thetaopt - theta))
              
    if (i % 10 == 0):
        plt.plot(thetaopt[0], thetaopt[1], '.', color ='red')
        #print(fun(thetaopt))

    if (error < e).all():   # GENERADOR DE CORTE
        break
    
    i +=1    
    theta = thetaopt
       
plt.plot(thetaopt[0], thetaopt[1], 'o', color ='green')
plt.show()

#ACLARACION
''' EN ESTE CASO VEREMOS A LA GRAFICA DE LA FUNCION COMO UN MAPA DE RELIEVES, EN LA CUAL, LOS
COLORES MAS CLAROS COMO EL AMARILLO SERAN LOS MAXIMOS DE LA FUNCION, Y LOS COLORES OSCUROS, COMO
EL AZUL SERAN LOS MINIMOS DE LA FUNCION, EL CODIGO ESTA PREPARADO PARA QUE CORTE CUANDO
ENCUENTRE UN MINIMO O BIEN QUIERA SEGUIR BUSCANDO.
-------------------------------------------------------------------------------------
LA BUSQUEDA DEL MINIMO EN LA GRAFICA SE VERA REFLEJADO COMO:
 . UN PUNTO BLANCO COMO EL INICIO DE LA BUSQUEDA
 . SU RECORRIDO EN COLOR ROJO
 . UN PUNTO VERDE MOSTRANDO EL MINIMO DE LA FUNCION O COMO EL FINAL DE LA BUSQUEDA EN CASO DE NO ELEGIR CORTE
-------------------------------------------------------------------------------------
EN EL CASO DEL LR SE HA UTILIZADO UN NUMERO PEQUEÑO DEBIDO A QUE SI EL MISMO ES MAS GRANDE
EMPIEZA A PEGAR SALTOS SALTEANDO LOS MINIMOS DE LA FUNCION Y HASTA HACER QUE LA FUNCION LLEGUE
A PUNTOS MUY GRANDES HASTA INFINITOS AL PUNTO DE
CONVERGER'''
