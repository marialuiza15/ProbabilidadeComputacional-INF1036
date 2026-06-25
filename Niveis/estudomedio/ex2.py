import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

p = 0.06
n = 40 # quantidade de tentativas que nesse caso é o numero de cabnos da amostra

# A
# p(x=3)
prob_3 = binom.pmf(3, n, p)
print(prob_3*100)

# p(x>5)
prob_5 = 1 - binom.cdf(5,n,p)
print(prob_5*100)

# p(x<=4)
prob_4 = binom.cdf(4,n,p)
print(prob_4*100)


# B
valores_k = np.arange(0,41) #lista com todos os valores possiveis de k

amostra = binom.pmf(valores_k, n, p)

#plt.hist(amostra, bins=20)
#plt.show()

cont_3 = 0
cont_4 = 0
cont_5 = 0

amostra_sim = binom.rvs(n,p,size=50000) # gera lista de 50000 numeros entre 0 e n (40)

for i in amostra_sim:
    if i==3:
        cont_3+=1
    if i>5:
        cont_5+=1
    if i<=4:
        cont_4+=1

print(cont_3/50000*100)
print(cont_5/50000*100)
print(cont_4/50000*100)