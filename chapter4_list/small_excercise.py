catNames=[] #create an empty list

while True:
    print('Enter cat name'+ str(len(catNames)+1 )+ ' or enter nothing to stop:')
    name = input()
    if name == '': 
        break
    catNames = catNames + [name] #List concatenate


print('the catNames are:')
print(catNames)