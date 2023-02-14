#! /home/it_avng/.pyenv/shims/python3

'''
program design:  
run this program with a command line argument
that is a short key phrase—for instance, agree or busy
essage associated with that key phrase will be copied to 
the clipboard so that the user can paste it into an email.

'''

TEXT = {'agree': """Yes, I agree. That sounds fine to me """, 
        'busy' : """Sorry, Can I reschedule our meeting to a later date""",
        'upsell': """Would you consider subscribe to our channel?"""}

import sys
#sys.path('/home/it_avng/.pyenv/versions/3.11.2/envs/Automate.Boring.Stuff/lib/python3.11/site-packages/')

import pyperclip as ppc
keyPhrase = sys.argv[1] # first command line arg is the keyphrase
if len(sys.argv) <2:
    print('Usage: python3 mclip.py [keyPhrase] -copy phrase text')
    sys.exit()
    
if keyPhrase in TEXT:
    ppc.copy(TEXT[keyPhrase])
    print('Text for '+keyPhrase+' copied to clipboard.')
else:
    print('There is no text for the key Phrase')


