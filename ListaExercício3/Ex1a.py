import random
random.seed(123)

def LCG(a,c,M,x0,qtd,low=0,high=0):
    lista = []
    for _ in range(qtd):
        x0 = (a*x0+c)%M
        uk = x0/M

        if low==0 and high==0:
            lista.append(uk)

        else:
            resultado = low+(high-low)*uk
            lista.append(resultado)

    return lista,x0

def jogaMoeda(x0):
    prob, x0 = LCG(39373,0,2**31 - 1,x0,1,low=0,high=1)

    if prob[0]<0.5:
        return 1, x0
    else:
        return 0, x0

def simulacao():
    x0 = 3
    cara_coroa=0

    for i in range(10000):
        retA, x0 = jogaMoeda(x0)
        retB, x0 = jogaMoeda(x0)
        
        if (retA==1 and retB==0) or (retA==0 and retB==1):
            cara_coroa+=1

    print(cara_coroa)

simulacao()
# ---------------------

# import random
# random.seed(123)

# def aleatorioLCG(a, c, M, x0, qtd):
#     lista = []
#     for _ in range(qtd):
#         x0 = (a * x0 + c) % M
#         lista.append(x0 / M)
#     return lista

# def lancaMoedas():
#     a = 39373
#     c = 0
#     M = 2**31 - 1

#     m1 = aleatorioLCG(a, c, M, 3, 10000)
#     m2 = aleatorioLCG(a, c, M, 7, 10000)  # semente diferente

#     cara_coroa = 0

#     for probm1, probm2 in zip(m1, m2):
#         if (probm1 < 0.5 and probm2 >= 0.5) or (probm1 >= 0.5 and probm2 < 0.5):
#             cara_coroa += 1

#     print("Quantidade de lançamentos com cara e coroa:", cara_coroa)

# lancaMoedas()
