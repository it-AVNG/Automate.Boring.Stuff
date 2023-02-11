birthdays = {'Alice': 'Apr 1st', 'Bob': 'Dec 12th', 'Carol': 'Mar 4th'}


def updateDatabase(name, bday):
    birthdays[name] = bday
    print('Database updated')



while True:
  print('enter a Name (blank to quit):')
  name = input()
  if name == '':
      break
    
  if name in birthdays:
    print(name + ' birthday is: '+ birthdays[name])
  else:
    print('I dont have the birth day of '+ name)
    print('Input the birthday of '+ name + ' to the databse:')
    bday =input()
    updateDatabase(name, bday)
  
  ##print values of database
  print('database values are:')
  for v in birthdays.values():
     print(v)
  

  ##print keys of database
  print('database keys are:')
  for k in birthdays.keys():
     print(k)
  

  ##print items of the database
  print('database items are:')
  for key,value in birthdays.items():
     print('Key:' + key + ' Value: '+ value)
    

     
