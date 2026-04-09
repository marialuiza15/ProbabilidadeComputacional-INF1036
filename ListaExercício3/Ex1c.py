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

def LM(x0,lancamentos):
    bits=[]
    for _ in range(lancamentos):
        uk, x0=LCG(39373,0,2**31 - 1,x0,1,low=0,high=1)

        if uk[0]<0.5:
            bits.append(1) #cara
        else:
            bits.append(0) #coroa

    numeroFinal = 0
    tam = lancamentos-1
    for bit in bits:
        numeroFinal += bit*(2**tam)
        tam-=1
    
    return numeroFinal, x0

def lancaDadoViciado(x0):
    while True:
        numero, x0 = LM(x0, 10)

        indice = numero%7 #pq sao 7 faces possiveis
        faces = [1,2,4,5,6,7,8]
        
        return faces[indice], x0



def lancaMoedaDado():
    x0=3
    coroa_face8 = 0
    for _ in range(10000):
        moeda, x0 = LCG(39373,0,2**31 - 1,x0,1,low=0,high=1)
        dado,x0 = lancaDadoViciado(x0) 
        if dado==8 and moeda[0]<0.5:
            coroa_face8+=1

    print(coroa_face8)

lancaMoedaDado()


#------------

# import random
# random.seed(123)

# a = 39373
# c = 0
# M = 2**31 - 1

# def aleatorioLCG(a,c,M,x0,qtd):
#     lista=[]
#     for _ in range(qtd):
#         x0=(a*x0+c)%M
#         lista.append(x0/M)
#     return lista

# def aleatorioLM(x0):
#     bits = []

#     for _ in range(10):
#         x0 = (a * x0 + c) % M
#         m = x0 / M

#         if m < 0.5:
#             bits.append(1)
#         else:
#             bits.append(0)

#     numero = 0
#     tam = 9
#     for bit in bits:
#         numero += bit * (2 ** tam)
#         tam -= 1

#     return numero, x0


# def moedaVsDado():
#     moedas = aleatorioLCG(a,c,M,3,10000)

#     x0 = 3
#     faces_validas = [1, 2, 4, 5, 6, 7, 8]

#     dados = []
#     for _ in range(10000):
#         valor,x0 = aleatorioLM(x0)
#         indice = valor%7 #quantidade de faces
#         dado = faces_validas[indice]
#         dados.append(dado)
        
#     coroa_face8 = 0
#     for m, d in zip(moedas,dados):
#         if m<0.5 and d==8:
#             coroa_face8+=1

#     print("Quantidade de lançamentos com coroa e face 8:", coroa_face8)


# moedaVsDado()