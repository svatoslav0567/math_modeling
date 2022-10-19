a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (a + c > b) and (b + c > a):
  print('Треугольник существует')
if ((a == b) or (a == c) or (b == c)) and ((a + b > c) and (a + c > b) and (b + c > a)):
  print('Треугольник равнобедренный')
if a == b == c:
  print('Треугольник равносторонний')
if (a != b != c) and ((a + b > c) and (a + c > b) and (b + c > a)):
  print('Треугольник разносторонний')
if (a + b < c) and (a + c < b) and (b + c < a):
  print('Треугольника не существует')