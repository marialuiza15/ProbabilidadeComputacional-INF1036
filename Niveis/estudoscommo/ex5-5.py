import numpy as np
import matplotlib.pyplot as plt

lamb = 30
N = 10000

amostra = np.random.exponential(lamb, N)

media = amostra.mean()
desvp = amostra.std()

print(media, desvp) #valores muito proximos pois em distribuição exponmencial, por conta da variancia, media e desvio sao quase iguais.

plt.hist(amostra, bins=20)
plt.show()

