#This is a guess the number game.
import random
secno = random.randint(1, 20)
print('Iam thinking of a number between 1 and 20.')

#ask the player to guess 6 times.
for guesstaken in range(1, 7):
 print('Take a guess')
 guess = int(input())
 
 if guess < secno:
  print('Your guess is low')
 elif  guess > secno:
  print('your guess is  high')
 else:
  break #this condition is correct guess.
  
if guess == secno:
 print('Good job! You guessed my number in ' + str(guesstaken) + ' guesses!')
else:
 print('Nope, The number I  was thinkinng of was ' + str(secno)) 
