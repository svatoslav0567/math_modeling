def f(a, n):
  a0 = a
  for i in range(1, n):
    a = a * a0
  print(a)  
 

a = abs(int(input()))
n = int(input())
f(a, n)