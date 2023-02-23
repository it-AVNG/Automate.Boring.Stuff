import pyinputplus as pyip

def addUpToTen(numbers):
    numberList = list(numbers)
    for i, digit in enumerate(numberList):
      numberList[i] = int(digit)
    if sum(numberList) !=10:
       raise Exception('The digits must add up to ten, not %s' %
                       (sum(numberList)))
    return int(numbers)

response = pyip.inputCustom(addUpToTen)
    