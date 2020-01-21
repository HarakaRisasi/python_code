import os
import json

os.system('cls' if os.name == 'nt' else 'clear')

def get_username():
    """Get username"""
    # we have a file user.json
    filename = './json_ex/user.json'
    # program try opened file user.json into path "./json_ex/user.json" and use variable 'filename'
    try: 
        with open(filename) as f:
            # write in var 'user' the data was stored into this file 'user.json'
            user = json.load(f)    
    # If the program does not find the file "filename" then return NONE
    except FileNotFoundError:
        print("Error file was not found")
        return None
        
    else:
        return user

def greet_user():
    """Greeting user"""
    # make var "username" and var get data which was return from function 'get_username'
    username = get_username()
    # if such data was existed then print Greeating
    if username:
        print(f'Greeting {username}!')  
    # else then input new data from keyboard and make new file.json and write into file this new data
    else:   
        username = input("input your name: ")
        filename = './json_ex/user.json'
        with open(filename, 'w', encoding='utf-8') as fl:
            json.dump(username, fl, ensure_ascii=False)
            # print message
            print(f'We are save your name like a {username}!')

greet_user()