def printpicnic(itemsdict, leftwidth, rightwidth):
 print('PICNIC ITEMS'.center(leftwidth+rightwidth, '-'))
 for k, v in itemsdict.items():
  print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))
  
picnicitems = {'sandwiches': 4, 'burgers': 15, 'pizza':  5, 'mojito': 100}
printpicnic(picnicitems, 15, 5)
printpicnic(picnicitems, 100, 6)
