#differs from Javascript, the method of flaging in python

import re
#find all method return a list of all matched like global:
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'Cell: 415-555-9999 Work: 212-555-0000'
mo= phoneNumRegex.findall(message)
print(type(mo))

#flag DOTALL will math all with '.' including newline
newlineRegex = re.compile('.*', re.DOTALL)
string ='Serve the public trust.\nProtect the innocent.\nUphold the law.'
mo2= newlineRegex.search(string).group()
print(mo2)

#flag I will match all with case insensitivity
robocop = re.compile(r'robocop',re.I)
mo3 = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo3)

#adding multiple line and ignore case
phoneRegex = re.compile(r'''
                        (
                        (\d{3}|\(\d{3}\))?           # area code
                        (\s|-|\.)?                   # separator
                        \d{3}                        # first 3 digits
                        (\s|-|\.)                    # separator
                        \d{4}                        # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})? # extension
                        )
                          ''', re.VERBOSE|re.I)