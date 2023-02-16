'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password is defined as one that is at least eight characters long, 
contains both uppercase and lowercase characters, and has at least one digit. 
You may need to test the string against multiple regex patterns to validate its strength.
'''

import re
pwd='ngfw@s1428'

pwdRegex_min8=re.compile(r'[\S]{8,}')
pwdRegex_chr=re.compile(r'[\w]+')
pwdRegex = re.compile(r'[\w\d.-@!#$%\^&*]{8,}')
def isPwdstrong(string) :
    test = True
    check1 = pwdRegex_min8.findall(pwd)
    check2 = pwdRegex_chr.findall(pwd)
    if not check1:
      test = False
      print('not enough characters', end =' ')
      return test
    elif not check2:
      test = False
      return test
    return test

check = pwdRegex.findall(pwd)
print(check)
print('do my pwd strong enough?')
print(isPwdstrong(pwd))