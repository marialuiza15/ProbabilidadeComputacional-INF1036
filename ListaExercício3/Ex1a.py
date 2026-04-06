import random
random.seed(123)

def aleatorioLCG(a, c, M, x0, qtd):
    lista = []
    for _ in range(qtd):
        x0 = (a * x0 + c) % M
        lista.append(x0 / M)
    return lista

def lancaMoedas():
    a = 39373
    c = 0
    M = 2**31 - 1

    m1 = aleatorioLCG(a, c, M, 3, 10000)
    m2 = aleatorioLCG(a, c, M, 7, 10000)  # semente diferente

    cara_coroa = 0

    for probm1, probm2 in zip(m1, m2):
        if (probm1 < 0.5 and probm2 >= 0.5) or (probm1 >= 0.5 and probm2 < 0.5):
            cara_coroa += 1

    print("Quantidade de lançamentos com cara e coroa:", cara_coroa)

lancaMoedas()
