from pathlib import Path
print(Path('spam', 'bacon', 'eggs'))
myfiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myfiles:
    print(Path(r'~/repos/', filename))