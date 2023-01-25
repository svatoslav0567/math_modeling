import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 0.1)
def letaiga(v, t):
    dvdt = (gamma * v ** 2) / m - g
    return dvdt

v_0 = 20
m = 70
gamma = 0.5772
g = 9.81

	
v_t = odeint(letaiga, v_0, t)
plt.plot(t, v_t[:,0])
 
plt.savefig('letaiga')