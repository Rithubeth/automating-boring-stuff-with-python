birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', 'Carol': 'Mar 6'}
while True:
 print('Enter a name: (blank to quit)')
 name = input()
 if name == '':
  break
 if name in birthdays:
  print(birthdays[name] + 'is the birthday of ' + name)
 else:
  print('I dont have birthday info for ' + name)
  print('What is their birthday?')
  bday = input()
  birthdays[name] = bday
  print('database updated.')
  
