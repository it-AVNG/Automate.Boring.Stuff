def spam(divideby):
  try:  
    return 42 / divideby
  except ZeroDivisionError: 
    #the error name taken from the verbose feedback of the python debug code
    print('Error: invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))

