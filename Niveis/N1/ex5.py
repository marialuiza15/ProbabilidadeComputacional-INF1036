
# Exercício 1.5 — Geométrica pronta (preparação para Q5 da prova)

# Considere X∼ Geométrica com p=0.2 (probabilidade de "defeito" em cada teste).


# (a) Gere 100.000 amostras de XX
# X e estime P(X=6)
# P(X=6) contando quantos saíram iguais a 6.
# (b) Compare com o valor teórico P(X=6)=(1−p)5⋅p

# Em Python: np.random.geometric(p=0.2, size=N). Em R: rgeom(N, prob=0.2) + 1 (cuidado: R conta o número de falhas antes do primeiro sucesso, então some 1).

import numpy as np

p = 0.2
N = 100000

# na lembro como fazer a a e b

amostra = np.random.geometric(p,size=N)

#estimas P(x=6) 
p_estimado = np.mean(amostra==6)

#valor teorico
p_teorico = (1-p)**5 * p

print(f"Simulado: {p_estimado:.4f}")
print(f"Teórico:  {p_teorico:.4f}")