def estimar_numero_de_maquina():
    epsilon = 1
    while 1 + epsilon != 1:
        epsilon /= 2
    print('Numero de maquina', epsilon/2)


if __name__ == '__main__':
    estimar_numero_de_maquina()