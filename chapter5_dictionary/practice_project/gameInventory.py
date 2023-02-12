# The data structure to model the player’s inventory will be a dictionary 
# where the keys are string valuesdescribing the item in the inventory
#  and the value is an integer valuedetailing how many of that item the player has
# . For example,{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Write a function named displayInventory() : 
# take any possible“inventory” and display it prettily
# 

import pprint

#create an empty dictionary of inventory
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


#update inventory
#main program

def displayinventory(chest):
  print("Inventory:")
  item_total = 0
  for k, v in inventory.items():
    print(str(v) + ' ' + k)
    item_total += v
  print('Total number of items: ' + str(item_total))


displayinventory(inventory)