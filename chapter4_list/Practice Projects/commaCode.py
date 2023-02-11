# Say you have a list value like this:spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. 

import os, gc
#automatic garbage collecting
gc.enable()

list=[]

##create a clear screen method
def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

##method for Updating the list
def updateList(): 
    end = False
    while True:
      print('please input list item, input end to stop')
      item = input()
      if item == 'end':
         break
      list.append(item)
    
    clear() # clear screen

##ToDO: method for remove item in the List

##ToDo: Method for look up in the List

updateList()
#reiterate the input after clear screen
print('your list is:', end='')
print(list)

print('comma Code for the list:')
string ='' 

# update the string
for i in range(len(list)):
  if i!= (len(list)-1):
    string = string + str(list[i])+','
  else:
    string = string[0:-1] + ' and ' + str(list[i]) + '.'

print(string)



    