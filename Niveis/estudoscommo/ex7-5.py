import numpy as np
import matplotlib.pyplot as plt

def inversa(x):
    return np.sqrt(x)

N = 10000
amostra = np.random.uniform(0,1, N)

x = inversa(amostra)


print(x)
plt.hist(x, bins=20)
plt.show()