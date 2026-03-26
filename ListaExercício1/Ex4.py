import random
random.seed(123)

def embarque_passageiro():
    qtd_compareceu = 0
    qtd_fila_espera = 0
    qtd_overbooking = 0
    disct_custo = {"voluntarios": [0,0], "forcados": [0,0]}
    for i in range(100): #qtd dias
        for i in range(20): #qtd voos diarios
            for i in range(190): #qtd de passagens por voo
                probabilidade_de_comparecer = random.uniform(0,100)
                if qtd_compareceu<=180:
                    if probabilidade_de_comparecer<=95: #95%?
                        qtd_compareceu+=1
                else:
                    probabilidade_excedentes = random.randint(0, 100)
                    if probabilidade_excedentes<=25:
                        qtd_fila_espera +=1
                        disct_custo["voluntarios"][0]+=1 #qtd
                        disct_custo["voluntarios"][1]+=1000 #custo
                    else:
                        qtd_fila_espera +=1
                        disct_custo["forcados"][0]+=1 #qtd
                        disct_custo["forcados"][1]+=2500 #custo
            if (qtd_fila_espera):
                qtd_overbooking +=1
            qtd_compareceu=qtd_fila_espera
            qtd_fila_espera=0


    return disct_custo, qtd_overbooking

disct_qtd_custo, qtd_overbooking = embarque_passageiro()
qtd_vol = disct_qtd_custo.get("voluntarios")[0]
qtd_forc = disct_qtd_custo.get("forcados")[0]
custo_vol = disct_qtd_custo.get("voluntarios")[1]
custo_forc = disct_qtd_custo.get("forcados")[1]
custo_medio_diario = (custo_vol+custo_forc)/(100)

# calcule: 
# a taxa média de overbooking; 
# o custo total e 
# o custo médio diário das compensações; 
# quantos passageiros foram realocados voluntariamente e quantos foram forçados.

print(f"Quantidade de overbooking: {qtd_overbooking}")
print(f"Custo total de compensaçoes: {custo_vol+custo_forc}")
print(f"Custo médio diário de compensaçoes: {custo_medio_diario}")
print(f"Qtd de voluntarios: {qtd_vol}, Qtd de forçados: {qtd_forc}")