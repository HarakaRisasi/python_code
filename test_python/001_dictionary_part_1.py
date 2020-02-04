#Import library
import json

# Load the data, and just check if data loaded correctly.
# Try typing "type(data)" in terminal after executig firs two line of this snippet
data = json.load(open("data.json"))

# Function for retrieving definition
def retrive_definition(word):
    return data[word]

# Input from user
word_user = input("Enter a word: ")

# Retrive the definition using function and print the result
print(retrive_definition(word_user))