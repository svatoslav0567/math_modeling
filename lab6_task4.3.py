import matplotlib.pyplot as plt
import numpy as np

phi = np.arange(0.01, 8 * np.pi, 0.01 )
r = 1 / phi**0.5

x = r * np.cos(phi)
y = r * np.sin(phi)
plt.plot(x, y)
plt.grid()
plt.savefig('jesl.png')