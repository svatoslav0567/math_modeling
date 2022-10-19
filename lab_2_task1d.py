a = int(input())
b = int(input())
c = int(input())
x1 = 0
x2 = 0
d = (b**2 - (4*a*c))
if d > 0:
  x1 = (-b + d**0.5)/2*a
  x2 = (-b - d**0.5)/2*a
  print('x1 = ', x1, 'x2 = ', x2)
elif d == 0:
  print('x=', -b/(2*a))
elif d < 0:
  print('Нет корней')
  