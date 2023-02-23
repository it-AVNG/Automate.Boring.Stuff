import pyinputplus as pyip
import random, time


numberOfQuestion= 10
correctAnswer = 0
for question in range(numberOfQuestion):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    promt = '#%s: %s x %s = ' %(question, num1, num2)
    try:
      pyip.inputStr(promt, allowRegexes=['^%s' %(num1*num2)],
                  blockRegexes=[('.*', 'Incorrect!')],
                  timeout = 8, limit=3)
    except pyip.TimeoutException: print('Out of time')
    except pyip.RetryLimitException: print('Out of tries')
    else:
       print('Correct!')
       correctAnswer+=1
    time.sleep(0.5)

print('score: %s /%s' %(correctAnswer, numberOfQuestion))
