import random
random.seed(123)


def dueloFinal(x,y,px,py):
    return random.choices([x,y], weights=(px,py))[0]

def duelo():
    descansado = random.choices(['A','B','C'], weights=(0.4,0.3,0.3))[0]

    if descansado=='A':
        vencedor = random.choices(['B','C'], weights=(0.65,0.35))[0]
        if vencedor == 'B':
            return dueloFinal('A','B',0.60,0.40)
        else:
            return dueloFinal('C','A',0.55,0.45)

    if descansado=='B':
        vencedor = random.choices(['C','A'], weights=(0.55,0.45))[0]
        if vencedor == 'C':
            return dueloFinal('B','C',0.65,0.35)
        else:
            return dueloFinal('A','B',0.60,0.40)

    if descansado=='C':
        vencedor = random.choices(['A','B'], weights=(0.60,0.40))[0]
        if vencedor == 'A':
            return dueloFinal('C','A',0.55,0.45)
        else:
            return dueloFinal('B','C',0.65,0.35)

d = {'A':0,'B':0,'C':0}
for _ in range(1000):
    campeao = duelo()
    d[campeao] +=1

print(f"A probabilidade de cada lutador vencer a etapa:\nA: {d.get('A')/1000}\nB: {d.get('B')/1000}\nC: {d.get('C')/1000}")

# ----------------------------

# import random
# random.seed(123)


# def duelo():
#     dict_vencedor={'A':0, 'B':0, 'C':0}
#     for i in range(1000):
#         probabilidade_vitoria = random.randint(0, 100)
#         probabilidade_descanso = random.randint(0, 100)
        

#         if i==0:
#             if probabilidade_descanso <=40:
#                 jogador_espera = ['A']
#             else:
#                 jogador_espera = random.choices("BC", k=1)
#         else:
#             jogador_espera = random.choices("ABC", k=1)

#         print("Em descanso: ",jogador_espera)

#         if jogador_espera[0]=='C':
#             if probabilidade_vitoria <=60: #0.6%
#                 print("A vence B")
#                 dict_vencedor['A']+=1
#             else: #0.4%
#                 print("B vence A")
#                 dict_vencedor['B']+=1

#         elif jogador_espera[0]=='A':
#             if probabilidade_vitoria <=65: #0.65%
#                 print("B vence C")
#                 dict_vencedor['B']+=1
#             else: #0.35%
#                 print("C vence B")
#                 dict_vencedor['C']+=1

#         elif jogador_espera[0]=='B':
#             if probabilidade_vitoria <=55: #0.55%
#                 print("C vence A")
#                 dict_vencedor['C']+=1
#             else: #0.45%
#                 print("A vence C")
#                 dict_vencedor['A']+=1
#     return dict_vencedor

# dict = duelo()
# print("\n\n")

# #estimar a probabilidade de cada lutador vencer a etapa

# probA = dict['A']/1000;
# probB = dict['B']/1000;
# probC = dict['C']/1000;

# print(f"Probabilidade de vencer, para cada jogador: \n A:{probA*100}%\n B:{probB*100}%\n C:{probC*100}%")