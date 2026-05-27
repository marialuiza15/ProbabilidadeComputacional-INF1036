#ERRADO

import random
random.seed(123)

def define():
    d = {'A':0,'B':0,'C':0,'D':0}
    l_jogadores = random.sample(['A','B','C','D'], k=2)
    j1 = l_jogadores[0]
    j2 = l_jogadores[1]

    if j1=='A':
        if j2 =='B':
            venceu = random.random() <= 0.55
            if(venceu):
                d['A']+=1
            else:
                d['B']+=1

        if j2 =='C':
            venceu = random.random() <= 0.45
            if(venceu):
                d['A']+=1
            else:
                d['C']+=1

        if j2 =='D':
            venceu = random.random() <= 0.60
            if(venceu):
                d['A']+=1
            else:
                d['D']+=1
        
    if j1=='B':
        if j2 =='C':
            venceu = random.random() <= 0.50
            if(venceu):
                d['B']+=1
            else:
                d['C']+=1

        if j2 =='D':
            venceu = random.random() <= 0.65
            if(venceu):
                d['B']+=1
            else:
                d['D']+=1

    if j1=='C':
        if j2 =='D':
            venceu = random.random() <= 0.70
            if(venceu):
                d['C']+=1
            else:
                d['D']+=1

    return d

d = {'A':0,'B':0,'C':0,'D':0}

for _ in range(1000):
    di = define()
    d['A']+=di['A']
    d['B']+=di['B']
    d['C']+=di['C']
    d['D']+=di['D']

print("Probabilidade de cada um vender o torneio: ")
print("A: ", d['A']/1000)
print("B: ", d['B']/1000)
print("C: ", d['C']/1000)
print("D: ", d['D']/1000)