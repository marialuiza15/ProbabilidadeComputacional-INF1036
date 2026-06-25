import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

lam = 18

# A
prob_a = poisson.pmf(22, lam) 
print(prob_a*100)


