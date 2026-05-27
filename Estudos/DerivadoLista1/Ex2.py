import random
random.seed(42)

def ciclo_vida():
    vida_util = 1
    subs = 0
    custo = 0
    num_falhas = 0

    for _ in range(500): #horas
        reducao = random.choices([0.02,0.05,0.1], k=1, weights=[60,30,10])[0]
        falha_repentina = random.random()<0.005
        
        if(falha_repentina): 
            custo += 3500
            subs +=1
            vida_util = 1
            num_falhas +=1
            continue

        
        vida_util-=reducao
        match(reducao*100):
            case 2:
                custo += 300
            case 5:
                custo += 600
            case 10:
                custo += 1200

        if(vida_util<=0.0):
            subs +=1
            vida_util = 1

    return (custo, subs, num_falhas)
            
subs_sim = 0
custo_sim = 0
falhas_sim = 0
for _ in range(1000):
    custo, subs, num_falhas = ciclo_vida()
    subs_sim += subs
    custo_sim += custo
    falhas_sim += num_falhas

print(f"A média de substituições por simulação: {subs_sim/1000}")
print(f"O custo médio total por simulação.: {custo_sim/1000}")
print(f"O número médio de falhas elétricas repentinas: {falhas_sim/1000}")
