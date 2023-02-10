supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

def browsing(stock):
    for index, supply in enumerate(stock):
      print('at index ' + str(index) + ' is item ' + supply)
browsing(supplies)

while True:
  try: 
    print('add a supply to the list (or nothing to quit):', end ='')
    item = input()
    if item == '' : 
      break
    print('do you have specific index? (or nothing to append at the end):', end ='')
    place = input()

    if place == '':
      supplies.append(item)
    else:
      supplies.insert(int(place), item)

    browsing(supplies)
  except ValueError: 
    print('such place do not exist, please type integers only')
    continue


