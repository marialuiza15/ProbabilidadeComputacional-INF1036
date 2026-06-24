import random

random.seed(123)

def lcg(x_anterior, a, c, M, n):
    l = []

    for i in range(n):
        x = (a*x_anterior + c)%M
        x_anterior = x

        uk = x/M

        l.append(uk)

    print(l)

lcg(3, 4, 1, 9, 12) # no 10° indice a sequencia reinicia
# periodo = 10