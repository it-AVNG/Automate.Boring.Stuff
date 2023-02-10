supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
print('list of available supply:')
for supply in supplies:
  print('-' + supply)


while True:
  print('enter a supply (or nothing to quit): ')
  name = input()
  if name == '':
     break
  if name not in supplies:
      print('supply you are looking for is not available')
  else:
      print(name + ' is available')