import random

random.seed(123)

def calcula_area(x1,y1,x2,y2,x3,y3):
    return(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2

def verifica_qualidade(proporcao):
    if proporcao<0.05: return "Ruim"
    if 0.05<=proporcao<0.1: return "Média"
    if 0.1<=proporcao<0.2: return "Boa"
    if proporcao>=0.2: return "Excelente"

def estima_cobertura():
    x1 = random.uniform(0,100)
    y1 = random.uniform(0,100)
    x2 = random.uniform(0,100)
    y2 = random.uniform(0,100)
    x3 = random.uniform(0,100)
    y3 = random.uniform(0,100)
    proporcao = calcula_area(x1,y1,x2,y2,x3,y3)/(100*100)
    
    return verifica_qualidade(proporcao)

d_qual_qtd = {"Ruim":0, "Média":0, "Boa":0, "Excelente":0}

for _ in range(1000):
    qual = estima_cobertura()
    d_qual_qtd[qual]+=1

print("Probabilidades:")
for k in d_qual_qtd:
    print(f"{k}: {d_qual_qtd[k]/1000:.3f}")