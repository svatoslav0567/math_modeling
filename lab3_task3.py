import numpy as np
from constants import g

x0 = int(input())
y0 = int(input())
v0x = int(input())
v0y = int(input())

t = np.arange(0, 5, 0.1)

x = x0 + v0x * t
y = y0 + v0y * t - (g * t ** 2 / 2)

coords = np.zeros((len(t), 3))
for i in range(len(t)):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]

print(coords)