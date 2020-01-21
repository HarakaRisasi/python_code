import os
import json

os.system('cls' if os.name == 'nt' else 'clear')


filename = './json_ex/user.json'

# program opened file "filename" into "./json_ex/user.json"
try: 
    with open(filename) as fl:
        user = json.load(fl)

# If the program does not find the file "filename" then it creates a new file
except:
    user = input("input your name: ")
    with open(filename, 'w', encoding='utf-8') as fl:
        json.dump(user, fl, ensure_ascii=False)
        print(f'We are save your name like a {user}!')

# If the program was able to open the file then print message
else:
    print(f"Greating {user}!")