# Write a function named addToInventory(inventory, addedItems), where the
# inventory parameter is a dictionary representing the player’s inventory


inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToinventory(inv,addItems):
  for item in addItems:
    inv.setdefault(item,0)
    inv[item] +=1
  return inv

def displayinventory(chest):
  print("Inventory:")
  item_total = 0
  for k, v in chest.items():
    print(str(v) + ' ' + k)
    item_total += v
  print('Total number of items: ' + str(item_total))





inventory = addToinventory(inventory,dragonLoot)
displayinventory(inventory)