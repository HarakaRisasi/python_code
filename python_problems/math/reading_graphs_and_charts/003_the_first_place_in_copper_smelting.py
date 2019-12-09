# The first place in copper smelting

# The chart shows the distribution of copper smelting 
# in 11 countries (thousands of tons) for 2006. 
# Papua New Guinea was the first country to splinter in copper 
# smelting and India was ranked eleventh. What was Portugal's place?

# import linux console comand 'clear'
import subprocess
subprocess.call("clear")

from collections import OrderedDict 

# dictionary (key : value)
world_place = {
    'Argentina' : 170,
    'Bulgaria' : 100,
    'Brazil' : 145,
    'India' : 40, 
    'Laos' : 60, 
    'Mongoly' : 140, 
    'Papua new guinea' : 195,
    'Portugal' : 80, 
    'Uzbekistan' : 105,
    'Sweden' : 90,
    'South Africa' : 95
    }

# sort dict by value
place_in_copper_smelting = OrderedDict(sorted(world_place.items(), key=lambda item: item[1], reverse=True))

# from the dict made a list, numbered from digit one
for i, j in enumerate(list(place_in_copper_smelting), start= 1):
    print(i, j)
#>>
# 1 Papua new guinea
# 2 Argentina
# 3 Brazil
# 4 Mongoly
# 5 Uzbekistan
# 6 Bulgaria
# 7 South Africa
# 8 Sweden
# 9 Portugal
# 10 Laos
# 11 India