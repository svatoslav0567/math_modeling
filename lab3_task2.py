import numpy as np
from constants import *
h = 100
alfa = np.pi / 3
beta = 30

v = ((g * h * np.tan(beta) ** 2) / (2 * np.cos(alfa) ** 2 * (1 - np.tan(beta) * np.tan(alfa)))) ** 0.5
                                   
print(v)
T = 200
q = 300 

N = 2 / np.pi ** 0.5 * (h / (k * T) ** 3 / 2) * np.exp(-q / (k * T)) * q ** (T / 2)
print(N)