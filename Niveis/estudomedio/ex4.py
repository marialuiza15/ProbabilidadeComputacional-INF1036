import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

b = 2
s = 1500

# A
prob_a = 1 - weibull_min.cdf(1000, c=b, scale=s)
print(prob_a*100)

# B
# cdf calcula prob e pdf ploota
# pdf é a curva e c df é o resultado da probabilidad eportante a area pintada abaixo da curav

# P(x<800)
prob = weibull_min.cdf(800, c=b, scale=s)
print(prob*100)
# cria mil pontos de 0 ate 30000 pro eixo hgorizontal do grafico
x = np.linspace(0, 4000, 1000)

# calcula a altura dsa curva pdf em cadaum desses mil pontos
y = weibull_min.pdf(x, c=b, scale=s)

plt.plot(x, y) # desenha a curva pdf ligando os pontos (x,y)
plt.fill_between(x, y, where=(x <= 800)) # pinta a area debaixo da curva
#plt.show()


# C
b = 0.5
prob = weibull_min.cdf(800, c=b, scale=s)
print(prob*100)
# cria mil pontos de 0 ate 4000 pro eixo hgorizontal do grafico
x = np.linspace(0, 4000, 1000)

# calcula a altura dsa curva pdf em cadaum desses mil pontos
y = weibull_min.pdf(x, c=b, scale=s)

plt.plot(x, y) # desenha a curva pdf ligando os pontos (x,y)
plt.fill_between(x, y, where=(x <= 800)) # pinta a area debaixo da curva
plt.show()
