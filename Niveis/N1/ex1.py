# Exercício 1.1 — Geração e histograma

# Gere uma amostra de tamanho 10.000 de uma distribuição Uniforme(0, 1) 
# usando a função pronta da linguagem (np.random.uniform em Python ou runif em R) 
# e plote um histograma. Confirme visualmente que ele fica "achatado".

# Dica: import numpy as np; import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

N = 10000

amostra = np.random.uniform(0,1) # isso gera UM NUMERO. Para gerar uma amostra, é preciso um for
amostra = np.random.uniform(0,1, size=N) # isso gera varios

# Para plotar o histograma:
plt.hist(amostra, bins=30)
plt.show()

# ======> quase toda função do np.random precisa do size.