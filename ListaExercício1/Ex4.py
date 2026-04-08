import random
random.seed(123)

def embarque():
    fila = 0
    passageirosEmbarcados = 0
    passageirosOverbooking= {'voluntarios':[0,0], 'forçados':[0,0], 'overbooking':0}
    for _ in range(20*100):
        passageirosEmbarcados = min(fila, 180)
        fila -= passageirosEmbarcados
        for _ in range(190):
            probEmbarque = random.uniform(0.90, 0.95)
            compareceu = random.random() < probEmbarque

            if(compareceu): 
                if passageirosEmbarcados<180:
                    passageirosEmbarcados +=1
                else:
                    excedente = random.choices(['voluntarios','forçados'], weights=(0.25,0.75))[0]
                    passageirosOverbooking[excedente][0] +=1
                    passageirosOverbooking['overbooking'] +=1
                    fila +=1

                    if excedente=='voluntario':
                        passageirosOverbooking[excedente][1] += 1000
                    else:
                        passageirosOverbooking[excedente][1] += 2500
    
    return passageirosOverbooking

d = embarque()

print(f"Taxa média de overbooking: {d.get('overbooking')/2000}")
print(f"Custo total das compensações: {d.get('voluntarios')[1]+d.get('forçados')[1]}")
print(f"Custo médio diário das compensações: {(d.get('voluntarios')[1]+d.get('forçados')[1])/100}")
print(f"Quantos passageiros foram realocados voluntariamente: {d.get('voluntarios')[0]}")
print(f"Quantos passageiros foram realocados forçadamente: {d.get('forçados')[0]}")

#--------------------------

# import random
# random.seed(123)

# def embarque_passageiro():
#     qtd_compareceu = 0
#     qtd_fila_espera = 0
#     qtd_overbooking = 0
#     disct_custo = {"voluntarios": [0,0], "forcados": [0,0]}
#     for i in range(100): #qtd dias
#         for i in range(20): #qtd voos diarios
#             for i in range(190): #qtd de passagens por voo
#                 probabilidade_de_comparecer = random.uniform(0,100)
#                 if qtd_compareceu<=180:
#                     if probabilidade_de_comparecer<=95: #95%?
#                         qtd_compareceu+=1
#                 else:
#                     probabilidade_excedentes = random.randint(0, 100)
#                     if probabilidade_excedentes<=25:
#                         qtd_fila_espera +=1
#                         disct_custo["voluntarios"][0]+=1 #qtd
#                         disct_custo["voluntarios"][1]+=1000 #custo
#                     else:
#                         qtd_fila_espera +=1
#                         disct_custo["forcados"][0]+=1 #qtd
#                         disct_custo["forcados"][1]+=2500 #custo
#             if (qtd_fila_espera):
#                 qtd_overbooking +=1
#             qtd_compareceu=qtd_fila_espera
#             qtd_fila_espera=0


#     return disct_custo, qtd_overbooking

# disct_qtd_custo, qtd_overbooking = embarque_passageiro()
# qtd_vol = disct_qtd_custo.get("voluntarios")[0]
# qtd_forc = disct_qtd_custo.get("forcados")[0]
# custo_vol = disct_qtd_custo.get("voluntarios")[1]
# custo_forc = disct_qtd_custo.get("forcados")[1]
# custo_medio_diario = (custo_vol+custo_forc)/(100)

# # calcule: 
# # a taxa média de overbooking; 
# # o custo total e 
# # o custo médio diário das compensações; 
# # quantos passageiros foram realocados voluntariamente e quantos foram forçados.

# print(f"Quantidade de overbooking: {qtd_overbooking}")
# print(f"Custo total de compensaçoes: {custo_vol+custo_forc}")
# print(f"Custo médio diário de compensaçoes: {custo_medio_diario}")
# print(f"Qtd de voluntarios: {qtd_vol}, Qtd de forçados: {qtd_forc}")