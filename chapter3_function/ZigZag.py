import time, sys
indent = 0 #space to indent
indentIncreasing = True #Wether the indentation is increasing or not

try:
  while True : 
    ##mainprogram
    print(' ' * indent, end ='')
    print('**********')
    time.sleep(0.1) #pause for 0.2 sec

    ##change direction instruction
    if indentIncreasing:
      indent = indent +1 
      if indent == 9:
        #change direction
        indentIncreasing = False
    else:
      #decrease number of space
      indent = indent -1 
      if indent == 0:
        #change direction
        indentIncreasing = True
    ##Continue to run in the loop
except KeyboardInterrupt:
  sys.exit()