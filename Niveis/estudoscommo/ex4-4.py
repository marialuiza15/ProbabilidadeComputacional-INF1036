import numpy as np
import matplotlib.pyplot as plt

p = 0.25
N = 100000
amostras = np.random.geometric(p,N)

print((amostras==3).sum()/N)