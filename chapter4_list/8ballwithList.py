import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

while True:
    print('play magic 8ball? (y/n)', end='')
    response = input()
    if response == 'y':
      print(random.choice(messages))
    else:
       break
