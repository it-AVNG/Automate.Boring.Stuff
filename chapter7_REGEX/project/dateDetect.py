
dValue= '28/05/1992'
import re

def checkMonth31(month,day,leap):
  if month == 2 and day == 29:
    if leap == True:
      valid == True
      return valid
  if month == 4 or month == 6 or month == 9 or month == 11:
    if day > 30:
      valid == False
      return valid
  valid = True
  return valid
  

def validDateType(date2Check, leap) :
  match, day, month, year = date2check
  if int(year) >2999 or int(year)<1000 :
      valid = False
      return valid
  else:
    if int(year) % 100 == 0:
      leap = leap
    if int(year) % 4 == 0:
      leap = True 
  if int(month)>12 or int(month) <1:
    valid = False
    return valid
  if int(day)> 31 or int(day)<1:
    valid = False
    return valid
  else:
    valid = checkMonth31(int(month),int(day),leap)
  return valid

# main program
dateRegex = re.compile(r'''(
([0-3][0-9]) #Date group
/            #separator
([01]\d)     #monthgroup
 /           #separator
([12]\d\d\d) #Yeargroup
)''',re.VERBOSE)


#look for match in Regex
model = dateRegex.findall(dValue)
modelScore = []
#validate each matching
for date2check in model:
  valid = True
  leap = False 
  valid = validDateType(date2check,leap)
  modelScore.append(valid)

print(modelScore)



