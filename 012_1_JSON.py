# JSON используется для обмена данными
import json

nums = [1, 'jk', 2, 4, 7, '2E']

# maked file like a json(write data into JSON file)
filename = './json_ex/nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f)

# load json file(read data from JSON file)
filename = './json_ex/nums.json'
with open(filename) as fl:
    nums_new = json.load(fl)

print(nums_new) #>> [1, 'jk', 2, 4, 7, '2E']