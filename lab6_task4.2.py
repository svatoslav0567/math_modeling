import matplotlib.pyplot as plt
import numpy as np

phi = np.arange(0, 8 * np.pi, 0.01 )
r = 10 * phi

x = r * np.cos(phi)
y = r * np.sin(phi)
plt.plot(x, y)
plt.grid()
plt.savefig('archimed.png')