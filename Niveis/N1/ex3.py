

# Exercício 1.3 — Probabilidade frequentista

# Simule 50.000 lançamentos de uma moeda honesta. Estime P(cara). 
# Depois faça o mesmo com N = 100, 1.000, 10.000, 100.000 e mostre como a 
# estimativa converge para 0,5.

# Dica: use np.random.choice([0,1], size=N) ou sample(c(0,1), N, replace=TRUE).

import numpy as np
import matplotlib.pyplot as plt

#para mostrar a convergencia precisamos fazer um loop
for N in [100, 1000, 10000, 100000]: # o for vai rodar 4 vezes, em cada vez n será um dos valores da lista
    # o loop serve só pra mudar o valor de n, para o random gerar a sequencia da amostra.
    lancamentos = np.random.choice([0,1], size=N) # temos um vetor com 0 e 1
    print(f"N={N:>7}: P(cara) ≈ {np.mean(lancamentos):.4f}")


#Você vai ver os valores se aproximando de 0,5 conforme N cresce — isso é a Lei dos Grandes Números.