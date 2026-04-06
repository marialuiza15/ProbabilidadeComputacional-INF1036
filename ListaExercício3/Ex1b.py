import random
random.seed(123)

def aleatorioLCG(a,c,M,x0,qtd):
    lista = []
    for _ in range(qtd):
        x0 = (a*x0+c)%M
        lista.append(x0/M)
    return lista

def jogaMoedaDado():
    a = 39373
    c = 0
    M = 2**31 - 1

    moeda = aleatorioLCG(a,c,M,3,10000)
    dado = random.choices([1,2,3,4,5,6,7,8], k=10000)

    coroa_face5 = 0
    
    for m1,d1 in zip(moeda,dado):
        if m1<0.5 and d1==5:
            coroa_face5+=1

    print("Quantidade de lançamentos com coroa e face 5:", coroa_face5)

jogaMoedaDado()