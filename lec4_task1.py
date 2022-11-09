def func(a):
  kol = 0
  for j in a:
    kol += j
  x = kol / len(a)
  print(x)
func([1, 4, 5])