import pprint #for print prettily

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    #argument of the achracter is passed to the dictionary, with default value at 0
    count.setdefault(character,0) 

    count[character] = count[character] +1

pprint.pprint(count)

