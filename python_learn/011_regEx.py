import os
os.system('cls' if os.name == 'nt' else 'clear')

import re
####################################################################################
txt = "01.1 Выращивание однолетних культур (21345)"

# find all only the cyrylic characters witout numbers
regEx = re.findall(r'[\u0400-\u04FF]', txt)
print(regEx)
#>> ['В', 'ы', 'р', 'а', 'щ', 'и', 'в', 'а', 'н', 'и', 'е', 'о', 'д', 'н', 'о', 'л', 'е', 'т', 'н', 'и', 'х', 'к', 'у', 'л', 'ь', 'т', 'у', 'р']

#find all words and numbers
regEx = re.findall(r'\w+', txt)
print(regEx)
#>> ['01', '1', 'Выращивание', 'однолетних', 'культур', '21345']

#find only the number in parentheses
regEx = re.findall(r'\(\w+\)', txt)
print(regEx)
#>> ['(21345)']

# convert a list to string
listToString = ' '.join(map(str, regEx))
print(listToString)
#>> (21345)

# remove the parentheses
remove = re.sub(r'[\(\)]', '', listToString)
print(remove)
#>> 21345
####################################################################################