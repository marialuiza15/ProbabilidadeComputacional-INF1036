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
            resultado = low + (high-low)*uk
            lista.append(resultado)

    return lista, x0

def geraPersonagens():
    a = 39373
    c = 0
    M = 2**31 - 1
    x0=3

    personagens={}

    for i in range(10):
        forca, x0 = LCG(a,c,M,x0,1, low=10, high=20)
        agilidade, x0 = LCG(a,c,M,x0,1, low=5, high=15)
        inteligencia, x0 = LCG(a,c,M,x0,1, low=8, high=18)

        personagens.update({
            i+1: [forca[0],agilidade[0],inteligencia[0]]
        })

    return personagens

d = geraPersonagens()

for i,atributos in d.items():
    print(f"{i}° personagem:\nForça: {atributos[0]} Agilidade: {atributos[1]} Inteligencia: {atributos[2]}\n")


#---------------------------------

#Xn = (axn+1 + b) mod m 


# a = 39373
# c = 0
# M = 2**31 - 1
# x0 = 3

# listaNumerosAleatorios = []
# for i in range(10):
#     aux = (a*x0+c) # x+1 = (a*x0+c)*mod M
#     Xprox = aux%M
#     x0=Xprox # x0 = x+1
#     listaNumerosAleatorios.append(Xprox)

# print(listaNumerosAleatorios)
# print("\n")
# # para transformas os numeros gerados, em numeros entre um determinado intervalo conhcido
# # é preciso normalizar(virar um numero entre 0 e 1) e escalonar para o intervalo desejado

# #Xn = valor gerado dentro da lista de valores
# #M m´podulo utilizado

# #Normalizando:
# listaNumerosAleatoriosNormalizadosEscalonados=[]
# min = 10
# max = 20
# for i in range(10):
#     resultado = min+(max-min)*listaNumerosAleatorios[i]/M
#     listaNumerosAleatoriosNormalizadosEscalonados.append(resultado)

# print(listaNumerosAleatoriosNormalizadosEscalonados)
# print("\n")

# #Agora, ajustando para o intervalo [min, max]
# #vamos usar a formular minimax: resultado = min+(max-min)*Normalizado


# def gerarNumerosAleatorios(a, c, M, x0, min, max):
#     lista = []
#     for i in range(10):
#         aux = (a*x0+c) # x+1 = (a*x0+c)*mod M
#         Xprox = aux%M
#         x0=Xprox # x0 = x+1
#         lista.append(Xprox)
    
#     listaNumerosAleatoriosNormalizadosEscalonados=[]

#     for i in range(10):
#         resultado = min+(max-min)*lista[i]/M
#         listaNumerosAleatoriosNormalizadosEscalonados.append(resultado)
    
#     return listaNumerosAleatoriosNormalizadosEscalonados

# a = 39373
# c = 0
# M = 2**31 - 1
# x0=3

# dict_jogador={}
# for i in range(10):
#     dict_jogador.update({
#         i+1: [gerarNumerosAleatorios(a, c, M, x0, 10, 20)[i], gerarNumerosAleatorios(a, c, M, x0, 5, 15)[i], gerarNumerosAleatorios(a, c, M, x0, 8, 18)[i]],
#     })

# for indice,lista in dict_jogador.items():

#     print(indice, lista)



