import json

username = input("input your name: ")

filename = './json_ex/user.json'
with open(filename, 'w') as fl:
    json.dump(username, fl)
    print(f'We are save your name like a {username}!')