import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

G = 6.67 * 10 ** -11
h = 400000
R = 6371000
M = 5.9722 * 10 ** 24
v_0 = 10
x = np.arange(0, h, 100)


def planeta(v, r):    
    dvdr = (G * M) / (v * r ** 2)
    return dvdr

vg = odeint(planeta, v_0, r)
plt.plot(r, vg[:,0])
 
plt.savefig('planeta.png')
