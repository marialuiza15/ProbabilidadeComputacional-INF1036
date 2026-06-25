import numpy as np

contador = 0

N = 100000

for i in range(1,N):
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)

    if (x*x+y*y)<=1:
        contador+=1

pi_estimado = 4*contador/N

print(pi_estimado)