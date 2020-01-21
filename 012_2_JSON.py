import os
os.system('cls' if os.name == 'nt' else 'clear')

import json

#input data from keyboard
username = input("input your name: ")

# maked file like a json(write data into JSON file)
filename = './json_ex/user.json'
# For JSON understanding cyrillic characters(Symbols)
# encoding="utf-8"
# ensure_ascii=False
with open(filename, 'w', encoding="utf-8") as fl: 
    json.dump(username, fl, ensure_ascii=False)
    print(f'We are save your name like a {username}!')