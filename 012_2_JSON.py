import json

#input data from keyboard
username = input("input your name: ")

# maked file like a json(write data into JSON file)
filename = './json_ex/user.json'
with open(filename, 'w') as fl:
    json.dump(username, fl)
    print(f'We are save your name like a {username}!')