import random

random.seed(123)

def onibus():
    embarcados = 0
    fila = 0
    d = {'voluntario':0, 'obrigado':0}
    custo=0
    ovbk =0

    for _ in range(10):
        if fila!=0:
            ovbk +=1
        embarcados = fila
        fila = 0

        for _ in range(55):
            p = random.uniform(0.80, 0.92)
            pass_emb = random.random() <= p

            if embarcados==50:
                fila+=1
                tipo_realocacao = random.choices(['voluntario', 'obrigado'], k=1, weights=[30,70])[0]

                if tipo_realocacao=='voluntario':
                    d['voluntario']+=1
                    custo +=150
                else:
                    d['obrigado']+=1
                    custo +=350

                continue

            if(pass_emb):
                embarcados +=1
    return(ovbk, custo, d)

qtd_ovbk = 0
custo_tol = 0
psg_vol = 0
psg_obg = 0
for _ in range(60):
    ovbk, custo, d = onibus()
    qtd_ovbk += ovbk
    custo_tol += custo
    psg_vol += d['voluntario']
    psg_obg += d['obrigado']

print("prob de overbooking por dia: ", ovbk/60)
print("O custo médio diário com compensações: ", custo_tol/60)
print("O total de passageiros reacomodados voluntária : ", psg_vol)
print("O total de passageiros reacomodados compulsoriamente : ", psg_obg)