import random, sys
print('Rock, Paper, Scissors')
wins = 0
losses = 0
ties = 0
while True:
 print('%s wins, %s losses, %s ties' % (wins, losses, ties))
 while True:
  print('enter your move: (r)rock (p)paper (s)scissors or (q)quit')
  playermove = input()
  if playermove == 'q':
   sys.exit()
  if playermove == 'r' or playermove == 'p' or playermove == 's':
   break
  print('Type one of r, q, s, or q.')

 if playermove == 'r':
  print('rock versus...')
 elif playermove == 'p':
  print('paper versus...')
 elif playermove == 's':
  print('scissors versus...')

 randno = random.randint(1, 3)
 if randno == 1:
  computermove =  'r'
  print('rock')
 elif randno == 2:
  computermove = 'p'
  print('paper')
 elif randno == 3:
  computermove = 's'
  print('scissors')
  
  #display and record the win/loss/tie:
 if playermove == computermove:
  print('Its a tie')
  ties = ties + 1
 elif playermove == 'r' and computermove == 's':
  print('You win')
  wins = wins + 1
 elif playermove == 'p' and computermove == 'r':
  print('You win')
  wins = wins + 1
 elif playermove == 's' and computermove == 'p':
  print('You win')
  wins = wins+ 1
 elif playermove == 'r' and computermove == 'p':
  print('You loss')
  losses = losses + 1
 elif playermove == 'p' and computermove == 's':
  print('You loss')
  losses = losses + 1
 elif playermove == 's' and computermove == 'r':
  print('You loss')
  losses = losses + 1 
