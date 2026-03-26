#Xn = (axn+1 + b) mod m 

'''
Os valores de Xn são interios entre 0 e m-1

a e b são sempre positivos

'''
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


def gerarNumerosAleatorios(a, c, M, x0, min, max):
    lista = []
    for i in range(10):
        aux = (a*x0+c) # x+1 = (a*x0+c)*mod M
        Xprox = aux%M
        x0=Xprox # x0 = x+1
        lista.append(Xprox)
    
    listaNumerosAleatoriosNormalizadosEscalonados=[]

    for i in range(10):
        resultado = min+(max-min)*lista[i]/M
        listaNumerosAleatoriosNormalizadosEscalonados.append(resultado)
    
    return listaNumerosAleatoriosNormalizadosEscalonados

a = 39373
c = 0
M = 2**31 - 1
x0=3

dict_jogador={}
for i in range(10):
    dict_jogador.update({
        i+1: [gerarNumerosAleatorios(a, c, M, x0, 10, 20)[i], gerarNumerosAleatorios(a, c, M, x0, 5, 15)[i], gerarNumerosAleatorios(a, c, M, x0, 8, 18)[i]],
    })

for indice,lista in dict_jogador.items():

    print(indice, lista)