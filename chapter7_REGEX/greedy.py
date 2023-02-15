import re
#greedy search is set as default, to be non-greedy, use ? at the end
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
greedyHaRegex = re.compile(r'(Ha){3,5}')