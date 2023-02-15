#! /home/it_avng/.pyenv/shims/python3

print('Enter the English message to translate into pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
piglatin = [] # A list of the words in Pig Latin. 
for word in message.split():
    
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0 :
        piglatin.append(prefixNonLetters)
        continue
    
    #separate the non-letters at the end of this word
    suffixNonletters = ''
    while not word[-1].isalpha():
        suffixNonletters +=word[-1]
        word =word[:-1]
    
    # Remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #make the word lowercase in translation

    #seperate consonant at the start of this word
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    #add Pig Latin ending 
    if prefixConsonants!= '':
        word += prefixConsonants+ 'ay'
    else:
        word += 'yay'

    #set the word back to uppercase or title case
    if wasTitle:
        word = word.title()
    if wasUpper:
        word = word.upper()
    
    #Add the non-letters bak to the start or end of the word
    piglatin.append(prefixNonLetters + word + suffixNonletters)

print(''.join(piglatin))

