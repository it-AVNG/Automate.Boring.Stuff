##write a short program, to guess a number between 0 and 20
##after 5 time wrong guessing, program will generate the response and restart
##type exit to quit

import random, sys 

while True:
    # generate the random number
    num = random.randint(0,20)

    #looking for the input
    print('guess the random number between 0 and 20: ')
    response = input()

    #check if input is equal to guess number 5 times
    for i in range(4):
      if response == num :
        print('congrats, you guessed right!')
      else:
        print('try again')
        #looking for the input
        response = input()

    #Give answer
    print('the answer is:' + str(num))
    #check if player want to continue
    print(' type continue to restart:')
    response = input()
    if response == 'continue':
       continue
    else:
        sys.exit()

