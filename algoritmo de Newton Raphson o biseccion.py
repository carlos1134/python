'''Implementar el siguiente algoritmo para hallar la raız de una funcion f en in intervalo real I = [a, b]:
Empieza en x0 = (a + b)/2 , el xn+1 es el de Newton Raphson en el caso en que xn+1 caiga en el
intervalo deseado y caso contrario usar biseccion. Recordar en cada paso redefinir el intervalo I en el
que tengo la raız'''


def newton_raphson_biseccion(f, f_derivada, a, b, rtol, maxiter=500, args=()):
    x = (a + b) / 2
    i = 0
    while abs(f(x, args[0])) > rtol and i < maxiter:
        if f_derivada != 0:
            x_new = x - f(x, args[0]) / f_derivada(x, args[0])
            if a < x_new < b:
                x = x_new
                if f(a, args[0]) * f(x, args[0]) < 0:
                    b = x
                else:
                    a = x
            elif f(x, args[0]) * f(a, args[0]) < 0:
                x = (x + a) / 2
                b = x
        i = i + 1
    return x

    
