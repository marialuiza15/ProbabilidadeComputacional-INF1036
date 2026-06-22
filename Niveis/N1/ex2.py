
# Exercício 1.2 — Estimando π (Monte Carlo clássico)

# Sorteie N = 100.000 pontos uniformes dentro do quadrado [−1,1]×[−1,1]. 
# Conte a fração que cai dentro do círculo de raio 1 centrado na origem. 
# Multiplique essa fração por 4 — você acabou de estimar pi

# Por que funciona? Área do círculo / área do quadrado = π/4\pi/4

import numpy as np
import matplotlib.pyplot as plt

N = 100000

amostrax = np.random.uniform(-1,1, size = N)
amostray = np.random.uniform(-1,1, size = N)

# para checar se esta dentro do circulo de raio 1 centrado na origem, temos x²+y2 <=1

dentro = (amostrax**2 + amostray**2)<=1 # isso é uma condição. dentro será um vetor de True e False com N posições

# com o vetor de true e false, podemos usar o np.mean para ver a proporção de true.

fracao = np.mean(dentro)

print(fracao)

# np.mean(condicao_booleana) te dá a proporção de vezes que a condição foi verdadeira.
