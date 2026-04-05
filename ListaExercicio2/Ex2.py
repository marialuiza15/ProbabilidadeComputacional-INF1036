import random
#random.seed(123)

def calcEE():
    prob = random.random()
    if prob<=0.3:
        return 3
    if 0.3<prob<=0.8:
        return 4
    if 0.8<prob<=1.0:
        return 6
    
def calcSE():
    prob = random.random()
    if prob<=0.25:
        return 4
    if 0.25<prob<=0.85:
        return 5
    if 0.85<prob<=1.0:
        return 7   
    
def calcCE():
    prob = random.random()
    if prob<=0.4:
        return 3
    if 0.4<prob<=0.8:
        return 4
    if 0.8<prob<=1.0:
        return 6 
    
def calcALI():
    prob = random.random()
    if prob<=0.2:
        return 7
    if 0.2<prob<=0.7:
        return 10
    if 0.7<prob<=1.0:
        return 15 
    
def calcAIE():
    prob = random.random()
    if prob<=0.35:
        return 5
    if 0.35<prob<=0.8:
        return 7
    if 0.8<prob<=1.0:
        return 10
    
def calcFA():
    prob = random.random()
    if prob<=0.2:
        return 1.05
    if 0.2<prob<=0.8:
        return 1.15
    if 0.8<prob<=1.0:
        return 1.25
    
def calcProdutividade():
    prob = random.random()
    if prob<=0.2:
        return 4
    if 0.2<prob<=0.8:
        return 5
    if 0.8<prob<=1.0:
        return 6

def calcCustoHora():
    prob = random.random()
    if prob<=0.2:
        return 80
    if 0.2<prob<=0.8:
        return 100
    if 0.8<prob<=1.0:
        return 120
   
    
def calculaAPF():
    EE = 0
    for _ in range(25):
        EE += calcEE()

    SE = 0
    for _ in range(20):
        SE += calcSE()

    CE = 0
    for _ in range(15):
        CE += calcCE()

    ALI = 0
    for _ in range(12):
        ALI += calcALI()

    AIE = 0
    for _ in range(12):
        AIE += calcAIE()

    FA = calcFA()

    produtividade = calcProdutividade()
    custoHora = calcCustoHora()

    pfNaoAjustado = EE+SE+CE+ALI+AIE
    pfAjustado = pfNaoAjustado * FA

    tempoEmHoras = produtividade * pfAjustado
    tempoEmSemanas = tempoEmHoras/40

    custo = tempoEmHoras * custoHora

    return {
        'PF Ajustado': pfAjustado,
        'Tempo em semanas':tempoEmSemanas,
        'Custo': custo
    }

auxD = {'total PFA':0, 'total semanas':0, 'total custo':0}
custoBaixo = 0
poucasSemanas = 0
for i in range(10000):
    dicionario = calculaAPF()
    auxD['total PFA'] += dicionario.get('PF Ajustado')
    auxD['total semanas'] += dicionario.get('Tempo em semanas')
    auxD['total custo'] += dicionario.get('Custo')

    if dicionario.get('Custo') <280000:
        custoBaixo +=1
    if dicionario.get('Tempo em semanas') <60:
        poucasSemanas +=1


print(f"O valor médio esperado dos Pontos de Função Ajustados (PFA): {auxD.get('total PFA')//10000}")
print(f"O tempo médio em semanas (40h/semana) para o desenvolvimento: {auxD.get('total semanas')//10000}")
print(f"O custo médio do sistema: {auxD.get('total custo')//10000}")
print(f"A probabilidade de o custo ser menor que R$ 280.000,00: {custoBaixo/100}")
print(f"A probabilidade de o tempo ser menor que 60 semanas: {poucasSemanas/100}")