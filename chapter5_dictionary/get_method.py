#get(keys,fallback_value)
birthdays = {'Alice': 'Apr 1st', 'Bob': 'Dec 12th', 'Carol': 'Mar 4th'}

print('enter name:', end= '')
name = input()
print('the data: ' + name + str(birthdays.get(name, 'is not available')))