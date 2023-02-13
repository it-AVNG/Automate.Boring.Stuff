# Useful method working with string

The upper(), lower(), isupper(), and islower() Methods

The isX() methods:
+ isalpha()	Returns True if all characters in the string are in the alphabet
+ isascii()	Returns True if all characters in the string are ascii characters
+ isdecimal()	Returns True if all characters in the string are decimals
+ isdigit()	Returns True if all characters in the string are digits
+ isidentifier()	Returns True if the string is an identifier
+ isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
+ istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

The startswith() and endswith() Methods:  return True if the string value they are called on begins or ends (respectively) with the string passed to the method;

The join() and split() Methods: check the example files
using block markdown code to pring strings with multiple lines
Splitting Strings with the partition() Method is also a split but return a tuple for the “before,” “separator,” and “after”.
You can use the multiple assignment trick to assign the three returned strings to three variables

Justifying Text with the rjust(), ljust(), and center() Methods:
+ add space/charactor to the right with string.rjust(int: number of character, str: character to add)
+ add space/charactor to the left with string.ljust(int: number of character, str: character to add)
+ add string to the center with string.center(int: number of character, str: character to add)

Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
Values of Characters with the ord() and chr() Functions
Copying and Pasting Strings with the pyperclip Module