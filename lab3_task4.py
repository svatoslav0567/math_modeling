import numpy as np
M = 5
N = 10
a = np.zeros((N, M))
for i in range(1, M):
  for j in range(1, M):
    a[i, j] = np.sin(N * i + M * j)
    if a[i, j] < 0:
      a[i, j] = 0

print(a)
    
    