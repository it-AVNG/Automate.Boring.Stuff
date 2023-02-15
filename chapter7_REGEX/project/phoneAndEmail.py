#! /home/it_avng/.pyenv/versions/3.11.2/envs/Automate.Boring.Stuff/bin/python
# phoneAndEmail.py finds phone numbers and email addresses on clipboard
# chmod u+x to turn it to executable 
import pyperclip,re

phoneRegex = re.compile(r'''(
                          (\d{3}|\(\d{3}\))?                 #areacode
                          (\s|-|\.)?                         #separator
                          (\d{3})                            #first 3 digits
                          (\s|-|\.)                          #separator
                          (\d{4})                            #last 4 digits
                          (\s*(ext|x|ext.)\s*(\d{2,5}))?     #extension
                        )''', re.VERBOSE)                   #flags

emailRegex= re.compile(r'''(
                          [a-zA-Z0-9._%+-]+    #Username
                          @                    # @ sympol
                          [a-zA-Z0-9._%+-]+    #domain name
                          (\.[a-zA-z]{2,5})+   #dot something maximum 5 letter, minimum 2 leter atleast once
                        )''',re.VERBOSE)

# TODO: Find matches in clipboard text.

text= str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
  matches.append(groups[0])

# TODO: Copy results to the clipboard.
if len(matches)>0 :
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No number or email was found')

