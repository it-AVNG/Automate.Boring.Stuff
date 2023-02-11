birthdays = {'Alice': 'Apr 1st', 'Bob': 'Dec 12th', 'Carol': 'Mar 4th'}

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
      birthdays[name] = bday
      print('Database updated')