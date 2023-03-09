allguests = {'Alice': {'apples': 5, 'peers': 2},
             'Bob': {'grape': 4, 'apple': 3},
             'Cev': {'pie': 1, 'grape': 10}}
def totalbrought(guests, item):
 numbrought = 0
 for k, v in guests.items():
  numbrought = numbrought + v.get(item, 0)
 return numbrought
print('number of things being brought:')
print('*apples     ' + str(totalbrought(allguests, 'apples')))
print('*peers      ' + str(totalbrought(allguests, 'peers')))
print('*grape      ' + str(totalbrought(allguests, 'grape')))
print('*pie        ' + str(totalbrought(allguests, 'pie')))
