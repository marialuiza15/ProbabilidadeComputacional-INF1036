import random
random.seed(123)

def definePouso():
    
    x = random.random()*100 #pois gerará entre 0 e 1, ou seja, entre 0 metros e 1 metro
    y = random.random()*100

    return (x,y)

def calculaAre(x1,y1,x2,y2,x3,y3):
    return (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2

def calculaQualidade(x):
    if x<0.05:
        return "Ruim"
    elif 0.05<=x<0.1:
        return "Média"
    elif 0.1<=x<0.2:
        return "Boa"
    else:
        return "Excelente"

def calculoPrincipal():
    x1,y1 = definePouso()
    x2,y2 = definePouso()
    x3,y3 = definePouso()

    area = calculaAre(x1,y1,x2,y2,x3,y3)

    proporcao = area/(100*100)
    return calculaQualidade(proporcao)

d = {}
qtd_simulacao = 1000

for _ in range(qtd_simulacao):
    qualidade = calculoPrincipal()
    if qualidade in d:
        d[qualidade] += 1
    else:
        d.update({
            qualidade: 1
        })

for qualidade,qtd in d.items():
    print(f"a probabilidade de ocorrência de cada categoria de qualidade de cobertura {qualidade}: {qtd/qtd_simulacao}")