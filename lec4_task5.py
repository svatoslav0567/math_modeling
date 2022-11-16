import numpy as np
def f(*args, **kwrgs):
  if kwrgs['figure'] != 'circle' or 'triangle' or 'rectangle': 
    s = "Погугли перевод"
  elif kwrgs['figure'] == 'circle':
    s = np.pi * args[0] ** 2
  elif kwrgs['figure'] == 'triangle':
    s = (args[0] * args[1]) / 2
  elif kwrgs['figure'] == 'rectangle':
    s = args[0] * args[1]
  print(s)

  
a = input()
f(4, 5, figure= a)
