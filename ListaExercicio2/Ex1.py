import random
#random.seed(123)

def calcDistribuicaoDados():
    probFloat = random.random()

    if probFloat<=0.2:
        return 2
    if 0.2<probFloat<=0.4:
        return 4
    if 0.4<probFloat<=1.0:
        return 3
    
def calcRequisitosDesempenho():
    probFloat = random.random()

    if probFloat<=0.1:
        return 3
    if 0.1<probFloat<=0.3:
        return 5
    if 0.3<probFloat<=1.0:
        return 4

def calcReusabilidade():
    probFloat = random.random()

    if probFloat<=0.1:
        return 1
    if 0.1<probFloat<=0.3:
        return 3
    if 0.3<probFloat<=1.0:
        return 2

def calcComplexibilidadeProcessamento():
    probFloat = random.random()

    if probFloat<=0.1:
        return 2
    if 0.1<probFloat<=0.2:
        return 5
    if 0.2<probFloat<=0.4:
        return 4
    if 0.4<probFloat<=1.0:
        return 3
    
def calcDemaisCaracteristicas():
    probFloat = random.random()

    if probFloat<=0.2:
        return 1
    if 0.2<probFloat<=0.4:
        return 3
    if 0.4<probFloat<=1.0:
        return 2
    
def calcProdutividade():
    probFloat = random.random()

    if probFloat<=0.2:
        return 4
    if 0.2<probFloat<=0.3:
        return 6
    if 0.3<probFloat<=1.0:
        return 5

def calcCustoHora():
    probFloat = random.random()

    if probFloat<=0.2:
        return 80
    if 0.2<probFloat<=0.4:
        return 120
    if 0.4<probFloat<=1.0:
        return 100

def calculaSomaCaracteristicas():
    
    distDados = calcDistribuicaoDados()
    reqDesempenho = calcRequisitosDesempenho()
    reusabilidade = calcReusabilidade()
    compProcessamento = calcComplexibilidadeProcessamento()

    somaCaracteristicas = distDados + reqDesempenho + reusabilidade + compProcessamento

    for i in range(10):
        somaCaracteristicas += calcDemaisCaracteristicas()

    FA = 0.65 + 0.01 * somaCaracteristicas
    PF = 3500 * FA

    produtividade = calcProdutividade()
    custoHora = calcCustoHora()

    tempoTotalHoras = PF * produtividade

    tempoSemanas = tempoTotalHoras/40
    custo = tempoTotalHoras * custoHora

    dicionario = {
        'PF': PF,
        'Tempo em Semanas': tempoSemanas,
        'Custo': custo
    }

    return dicionario

custoAlto = 0
custoSemanas = 0
totalPF = 0
for i in range(10000):

    dici = calculaSomaCaracteristicas()

    totalPF += dici.get('PF')

    if dici.get('Custo') <1500000:
        custoAlto +=1

    if dici.get('Tempo em Semanas') <450:
        custoSemanas +=1

print(f"O valor médio esperado de PF ajustado: {totalPF/10000}")
print(f"A probabilidade de o custo ser menor que R$ 1.500.000,00: {custoAlto/100}%")
print(f"A probabilidade de o tempo ser menor que 450 semanas: {custoSemanas/100}%")