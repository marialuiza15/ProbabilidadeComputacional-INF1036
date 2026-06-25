import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

p = 0.15

# A
# p(x=8)
prob_x8 = geom.pmf(8, p) #um número -> prob de ser =8
print(prob_x8*100)

# B
# p(x>4)
prob_xnao4 = 1 - geom.cdf(4, p)
print(prob_xnao4*100)

# C
amostra = geom.rvs(p, size=100000) # sorteia cem mil vezes com a probabilidade dada e usando o formato geom
print(amostra)

cont_1 = 0
cont_2 = 0

for i in amostra:
    if i==8:
        cont_1 +=1
    if i>4:
        cont_2 +=1

print(cont_1/100000*100)
print(cont_2/100000*100)