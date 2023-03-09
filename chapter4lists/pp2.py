import random
numberofstreaks = 0
coinflip = []
streak = 0
for exerimentnumber in range(10000):
 for i in range(100):
  coinflip.append(random.randint(0,1))
 for i in range(len(coinflip)):
  if i == 0:
   pass
  elif coinflip[i] == coinflip[i-1]:
   streak += 1
  else:
   streak += 0
  if streak == 6:
   numberofstreaks += 1
 coinflip = []
print('chance of streak: %s%%' % (numberofstreaks/(100*10000)))
