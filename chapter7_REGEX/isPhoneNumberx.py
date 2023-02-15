import re 

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'Call me at 415-555-1011 tomorrow.'
mo =phoneNumRegex.search(message)
print('phone number found:' + mo.group())