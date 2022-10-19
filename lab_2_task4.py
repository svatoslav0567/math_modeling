N = int(input())
a_0 = 1
a_1 = 1

for i in range(N):
  a_2 = a_0 + a_1
  print(a_2)
  a_0 = a_1
  a_1 = a_2



  
