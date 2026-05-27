import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(123)

def LCG(a,c,M,xo,qtd,low=0,high=0):
    lista = []
    for _ in range(qtd):
        xo = (a*xo+c)%M
        uk = xo/M

        if low==0 and high==0:
            lista.append(uk)

        else:
            resultado = low+(high-low)*uk
            lista.append(resultado)
    return lista, xo

def exibe(l):
    print("Cartas geradas com LCG: ")
    for i in range(15):
        print(f"{i+1}°: ",l[i])

def gera_atributos_LCG():
    
    a = 16807
    c = 0
    M = 2**31-1
    xo = 7

    
    l_cartas = []
    for _ in range(15):
        l_ataque, xo = LCG(a,c,M,xo,1,low=15,high=30)
        ataque = l_ataque[0]

        l_defesa, xo = LCG(a,c,M,xo,1,low=5,high=20)
        defesa = l_defesa[0]

        l_magia, xo = LCG(a,c,M,xo,1,low=0,high=10)
        magia = l_magia[0]

        l_cartas.append([ataque, defesa, magia])

    exibe(l_cartas)

    ataque = [c[0] for c in l_cartas]
    defesa = [c[1] for c in l_cartas]
    magia = [c[2] for c in l_cartas]

    return (ataque, defesa, magia)

def gera_atributos_Random():
    l_cartas = []

    for _ in range(15):
        ataque = random.uniform(15,30) 
        defesa = random.uniform(5,20)
        magia = random.uniform(0,10)

        l_cartas.append([ataque, defesa, magia])
    
    exibe(l_cartas)
    ataque = [c[0] for c in l_cartas]
    defesa = [c[1] for c in l_cartas]
    magia = [c[2] for c in l_cartas]

    return (ataque, defesa, magia)

def estatistica(nome, dados):
    print(f"\n{nome}")
    print("Média:", np.mean(dados))
    print("Desvio padrão:", np.std(dados))
    print("Min:", np.min(dados))
    print("Max:", np.max(dados))
    return

def hist(tit, dado1, dado2):
    plt.hist(dado1, alpha=0.5, label="LCG")
    plt.hist(dado2, alpha=0.5, label="Python")
    plt.title(tit)
    plt.legend()
    plt.show()
        
ataque_lcg, defesa_lcg, magia_lcg = gera_atributos_LCG()
print("\n")
ataque_py, defesa_py, magia_py = gera_atributos_Random()

estatistica("Ataque LCG", ataque_lcg)
estatistica("Ataque Python", ataque_py)

estatistica("Defesa LCG", defesa_lcg)
estatistica("Defesa Python", defesa_py)

estatistica("Magia LCG", magia_lcg)
estatistica("Magia Python", magia_py)

hist("Ataque", ataque_lcg,ataque_py)
hist("Defesa", defesa_lcg,defesa_py)
hist("Magia", magia_lcg,magia_py)
