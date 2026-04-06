import random
random.seed(123)

a = 39373
c = 0
M = 2**31 - 1

def aleatorioLCG(a,c,M,x0,qtd):
    lista=[]
    for _ in range(qtd):
        x0=(a*x0+c)%M
        lista.append(x0/M)
    return lista

def aleatorioLM(x0):
    bits = []

    for _ in range(10):
        x0 = (a * x0 + c) % M
        m = x0 / M

        if m < 0.5:
            bits.append(1)
        else:
            bits.append(0)

    numero = 0
    tam = 9
    for bit in bits:
        numero += bit * (2 ** tam)
        tam -= 1

    return numero, x0


def moedaVsDado():
    moedas = aleatorioLCG(a,c,M,3,10000)

    x0 = 3
    faces_validas = [1, 2, 4, 5, 6, 7, 8]

    dados = []
    for _ in range(10000):
        valor,x0 = aleatorioLM(x0)
        indice = valor%7 #quantidade de faces
        dado = faces_validas[indice]
        dados.append(dado)
        
    coroa_face8 = 0
    for m, d in zip(moedas,dados):
        if m<0.5 and d==8:
            coroa_face8+=1

    print("Quantidade de lançamentos com coroa e face 8:", coroa_face8)


moedaVsDado()