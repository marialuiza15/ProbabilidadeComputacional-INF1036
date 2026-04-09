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

def lancaMoeda(x0):
    moeda, x0 = LCG(39373,0,2**31 - 1,x0,1,low=0,high=1)
    if moeda[0]<0.5:
        return 1,x0
    else:
        return 0,x0
    
def lancaDado():
    return random.randint(1,8)

def lancaMoedaDado():
    x0 = 3
    coroa_face5 = 0
    for _ in range(10000):
        moeda, x0= lancaMoeda(x0)
        dado = lancaDado()

        if moeda==1 and dado==5:
            coroa_face5 +=1

    print(coroa_face5)

lancaMoedaDado()

# ---------------

# import random
# random.seed(123)

# def aleatorioLCG(a,c,M,x0,qtd):
#     lista = []
#     for _ in range(qtd):
#         x0 = (a*x0+c)%M
#         lista.append(x0/M)
#     return lista

# def jogaMoedaDado():
#     a = 39373
#     c = 0
#     M = 2**31 - 1

#     moeda = aleatorioLCG(a,c,M,3,10000)
#     dado = random.choices([1,2,3,4,5,6,7,8], k=10000)

#     coroa_face5 = 0
    
#     for m1,d1 in zip(moeda,dado):
#         if m1<0.5 and d1==5:
#             coroa_face5+=1

#     print("Quantidade de lançamentos com coroa e face 5:", coroa_face5)

# jogaMoedaDado()