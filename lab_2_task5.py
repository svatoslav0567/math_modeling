a = int(input())
b = int(input())
if a % b ==0 and b !=0:
  print('Делится,', f'частное {a // b}')
else:
  print('Не делится, ', f'остаток {a % b},', f'частное {a // b}')