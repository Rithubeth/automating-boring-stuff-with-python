n = int(input())
for i in range(1, n):
 if i%3== 0 and i%5== 0:
  print('carpool')
 elif i%5== 0:
  print('pool')
 elif i%3== 0:
  print('car')
 else:
  print(i)
