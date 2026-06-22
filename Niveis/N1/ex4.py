

# Exercício 1.4 — Exponencial pronta (preparação para Q3 da prova)

# Gere uma amostra de tamanho 10.000 de uma Exponencial com tempo médio 2 minutos 
# (ou seja, λ=1/2). Calcule a média e o desvio padrão da amostra — devem ficar 
# próximos de 2. 
# Plote o histograma.


# Em Python: np.random.exponential(scale=2, size=10000). Em R: rexp(10000, rate=1/2). Atenção: Python usa scale (= média = 1/λ), R usa rate (= λ).

# quando temos lambda, nao deveria ser poisson? pq a dica passa o exponential?

import numpy as np
import matplotlib.pyplot as plt

N=10000

amostra = np.random.exponential(scale=2, size=N) #sacel = 2 pois o enunciado diz 'com tempo médio 2 minutos '
print('media:', np.mean(amostra))
print('desvio:', np.std(amostra)) # em exponencial media = desvio em amostra infinita

plt.hist(amostra, bins="auto")  # usar o bins auto sempre, mas quqando for comparrar dois graficos, ai preciso passar o mesmo bin para os dois

plt.show()


'''
regras d ebiolso para nuemros bons de bins em histograma:

Tamanho da amostra / bins razoáveis
100                  10
1.000                20 a 30
10.000               30 a 60
100.000              50 a 100

'''