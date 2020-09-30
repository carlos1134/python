import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
from matplotlib import cm

A = np.matrix([[3.0, 2.0], [2.0, 6.0]])
b = np.matrix([[2.0], [-8.0]])  # usaremos la convención de que un vector es un vector de columna
c = 0.0

def f(x, A, b, c):
    return float(0.5 * x.T * A * x - b.T * x + c)

#mostraremos la grafica de f en 3d
def grafica_de_f(A, b, c):
    fig = plt.figure(figsize=(10,8))
    qf = fig.gca(projection='3d')
    size = 20
    x1 = list(np.linspace(-6, 6, size))
    x2 = list(np.linspace(-6, 6, size))
    x1, x2 = np.meshgrid(x1, x2)
    zs = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.matrix([[x1[i,j]], [x2[i,j]]])
            zs[i,j] = f(x, A, b, c)
    qf.plot_surface(x1, x2, zs, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
    fig.show()
    return x1, x2, zs

x1, x2, zs = grafica_de_f(A, b, c)

# con este metodo veriamos a f proyectado en contornos, con los pasos preparados a ejecutarse
def contoursteps(x1, x2, zs, pasos=None):
    fig = plt.figure(figsize=(6,6))
    cp = plt.contour(x1, x2, zs, 10)
    if pasos is not None:
        pasos = np.matrix(pasos)
        plt.plot(pasos[:,0], pasos[:,1], '-o')
    fig.show()

#preparamos las variables que vamos a utilizar para el gradiente conjugado
x = np.matrix([[-2.0],[-2.0]])
pasos = [(-2.0, -2.0)]
i = 0
imax = 10
eps = 0.01
r = b - A * x
d = r
deltanew = r.T * r
delta0 = deltanew

#gradiente conjugado
while i < imax and deltanew > eps**2 * delta0:
    alpha = float(deltanew / float(d.T * (A * d)))
    x = x + alpha * d
    pasos.append((x[0, 0], x[1, 0]))
    r = b - A * x           #este residual ya es usado con el x*
    deltaold = deltanew     # guardo el delta que tenia antes en un delta viejo
    deltanew = r.T * r      # este sera mi nuevo delta con el nuevo residual
    beta = float(deltanew / float(deltaold)) 
    d = r + beta * d
    i += 1

# mostramos el proceso y resultado en la grafica de contoursteps
contoursteps(x1, x2, zs, pasos)
