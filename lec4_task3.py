from constants import *
m = 40
h = 100
v = 25
def energy(m, h, g, v): 
  e1 = m * g * h
  e2 = (m * v ** 2) / 2
  E = e1 + e2
  print(E)
energy(m, h, g, v)
