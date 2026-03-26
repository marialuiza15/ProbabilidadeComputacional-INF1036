import random

#cada chamada a essa função significa uma execução de 720h
def simulacao():
    random.seed(123)
    vidautil = 1.0
    custo = 0
    contSubstituicao = 0
    custoSub=0
    falha=0
    for i in range(720):
        probabilidade = random.randint(0, 100)
        crash = random.randint(0, 1000)

        if 0<=crash<=2:
            vidautil = 1
            custo+=2000
            falha +=1
            contSubstituicao+=1

        if vidautil<=0:
            vidautil = 1
            custo += custoSub
            contSubstituicao+=1

        else:
            if probabilidade<=10:
                vidautil-=0.07
                custoSub = 700

            if 10<probabilidade<=30: 
                vidautil-=0.03
                custoSub = 500

            if 30<probabilidade<=100:
                vidautil-=0.01
                custoSub = 400

    return falha, custo, contSubstituicao

mediaSim=0
mediaCusto=0
totalFalhas=0
for i in range(1000):
    falha, custo, cont = simulacao()
    totalFalhas += falha
    mediaSim += cont
    mediaCusto += custo/cont

print("Media de substituições por simulação: ",mediaSim/1000)
print("Custo medio por simulação: ",mediaCusto/1000)
print("Quantidade total de falhas aleatorias: ",totalFalhas/1000)