while True:
 print('Enter your age:')
 age = input()
 if age.isdecimal():
  break
 else:
  print('please enter a number for your age.')

while True:
 print('Select a new password(letters and numbers only.):')
 password = input()
 if password.isalnum():
  break
 else:
  print('Password can only have letters and numbers.')
