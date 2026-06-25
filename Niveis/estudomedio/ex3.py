import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

# x = valor ate onde queremos acumular prob
mu = 80 #media da distribuicao
sigma = 18 #desvio padrao

# A
prob_a = norm.cdf(100, mu, sigma) - norm.cdf(60, mu, sigma)
print(prob_a*100)

# B
prob_b = 1 - norm.cdf(90, mu, sigma)
print(prob_b*100)

# C
# 1° probabilidade de um aluno terminar 4m menos de 70 min p(x<70)
prob_c = norm.cdf(70, mu, sigma)
print(prob_c*100)

#se cada aluno tem x chances de terminar a rpova em menos de 70 min
# entao 35 alunos tem essa mesma chance vezes 35

chance_35 = prob_c* 35

print(chance_35) #aqui é quantidade de alunos 

# D
cont = 0
amostra_sim = norm.rvs(loc=mu, scale=sigma, size=100000) #loc é media e scale é o desvio

for i in amostra_sim:
    if i>=60 and i<=100:
        cont+=1

print(cont/100000*100)