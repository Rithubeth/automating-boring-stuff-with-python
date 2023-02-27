passwordfile = open('secretpasswordfile.txt')
secretpassword = passwordfile.read().strip()
print("enter your password.")
typedpassword = input()
print(type(typedpassword), type(secretpassword))
if typedpassword == secretpassword:
 print('Access granted')
 if typedpassword == '12345':
  print("That password is one that an idiot puts on their luggage.")
else:
 print('Access denied') 
