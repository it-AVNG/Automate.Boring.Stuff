import re

#to subtitute a matched in regex we use sub() instead of search() property
agentname= re.compile(r'Agent (\w)\w*')
#the above statement is a regex pattern for 'Agent+(space)+(any word)+words
message = 'Agent Alice gave the secret documents to Agent Bob.'
censored = agentname.sub('CENSORED',message )
print(censored)
#we can subtitute the string with another regex string
censored = agentname.sub(r'\1****',message)
print(censored)


#typical managing REGEX scheme:
phoneRegex = re.compile(r'''
                        (
                        (\d{3}|\(\d{3}\))?           # area code
                        (\s|-|\.)?                   # separator
                        \d{3}                        # first 3 digits
                        (\s|-|\.)                    # separator
                        \d{4}                        # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})? # extension
                        )
                          ''', re.VERBOSE)