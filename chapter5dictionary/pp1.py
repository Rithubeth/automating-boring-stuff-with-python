stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayinventory(inventory):
 total = 0
 for k, v in inventory.items():
  print(str(v)+ ' ' + k)
  total += v
 print('total number of items: '+ str(total))
 
displayinventory(stuff)

def addtoinventory(inventory, addeditems):
 for item in addeditems:
  inventory.setdefault(item, 0)
  inventory[item] = +1
 return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addtoinventory(inv, dragonloot)
displayinventory(inv)
