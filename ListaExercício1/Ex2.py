import random
random.seed(123)

def calculaCustoDano(tipo, vida):
    if tipo == "Leve":
        return (400, vida-0.01)
    elif tipo == "Moderado":
        return (500, vida-0.03)
    else:
        return (700, vida-0.07)
    

def simulacao():
    lTipos = ["Leve", "Moderado", "Severo"]
    vidaUtil = 1.0
    d_controle = {'Leve': [0,0], 'Moderado': [0,0], 'Severo': [0,0], 'Total': [0,0]}
    for _ in range(720):

        falhaTotal = random.random()
        if falhaTotal<=0.002:
            vidaUtil = 0
            tipoDano = "Total"
            custo = 2000

        else:
            tipoDano = random.choices(lTipos, weights=(0.7,0.2,0.1))[0]
            custo, vidaUtil = calculaCustoDano(tipoDano, vidaUtil)
    

        if vidaUtil<=0:
            d_controle[tipoDano][0] += custo
            d_controle[tipoDano][1] += 1 #contador
            vidaUtil = 1

    return d_controle

media_substituicao = 0
media_custo = 0
media_falhas = 0
for _ in range(1000):
    d = simulacao()

    media_substituicao += (d.get('Leve')[1]+d.get('Moderado')[1]+d.get('Severo')[1]+d.get('Total')[1])
    media_custo += (d.get('Leve')[0]+d.get('Moderado')[0]+d.get('Severo')[0]+d.get('Total')[0])
    media_falhas += d.get('Total')[1]

print("A média de substituições por simulação: ", media_substituicao/1000)   
print("O custo médio total por simulação: ", media_custo/1000)
print("O número médio de falhas totais aleatórias: ", media_falhas/1000)           


# -------------------------

# import random

# #cada chamada a essa função significa uma execução de 720h
# def simulacao():
#     random.seed(123)
#     vidautil = 1.0
#     custo = 0
#     contSubstituicao = 0
#     custoSub=0
#     falha=0
#     for i in range(720):
#         probabilidade = random.randint(0, 100)
#         crash = random.randint(0, 1000)

#         if 0<=crash<=2:
#             vidautil = 1
#             custo+=2000
#             falha +=1
#             contSubstituicao+=1

#         if vidautil<=0:
#             vidautil = 1
#             custo += custoSub
#             contSubstituicao+=1

#         else:
#             if probabilidade<=10:
#                 vidautil-=0.07
#                 custoSub = 700

#             if 10<probabilidade<=30: 
#                 vidautil-=0.03
#                 custoSub = 500

#             if 30<probabilidade<=100:
#                 vidautil-=0.01
#                 custoSub = 400

#     return falha, custo, contSubstituicao

# mediaSim=0
# mediaCusto=0
# totalFalhas=0
# for i in range(1000):
#     falha, custo, cont = simulacao()
#     totalFalhas += falha
#     mediaSim += cont
#     mediaCusto += custo/cont

# print("Media de substituições por simulação: ",mediaSim/1000)
# print("Custo medio por simulação: ",mediaCusto/1000)
# print("Quantidade total de falhas aleatorias: ",totalFalhas/1000)