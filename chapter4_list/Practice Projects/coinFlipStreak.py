# Write a program to find out how often a streak of six heads or a streak
# of six tails comes up in a randomly generated list of heads and tails. Your
# program breaks up the experiment into two parts: the first part generates
# a list of randomly selected 'heads' and 'tails' values, and the second part
# checks if there is a streak in it. Put all of this code in a loop that repeats the
# experiment 10,000 times so we can find out what percentage of the coin
# flips contains a streak of six heads or tails in a row
# you’ll create a list that looks like “T T T T H H H H T T.”

import random, math

#initiate variable
list = []
headCount = 0
streak = 0
flipTime = 10000

#a function to flip the coind
def coinFlip():
    result = random.randint(0,1)
    if result == 0:
      return 'T'
    else:
       return 'H'

#main program

#loop the flipping 10K times
for i in range(flipTime):
  #flip the coin
  item = coinFlip()
  #tally the head
  if item == 'H':
    headCount += 1
  #if headCount reach 6, update streak and reset head count
  if headCount == 6:
     streak += 1
     headCount = headCount * 0
  #to update the list
  list.append(item) 

#Anouncing the streak

print('number of streak with 6 times Head is: ' + str(streak *100 /flipTime) + '%')


