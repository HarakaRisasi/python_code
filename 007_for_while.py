import subprocess
subprocess.call("clear")

# iterating over array elements with an index
animals = ['a', 'b', 'c']
for index in range(len(animals)):
    print(index, animals[index])
    #>> 
    # 0 a
    # 1 b
    # 2 c


for letter in 1, 3, 4:
    print(letter)
    #>> 
    # 1
    # 3
    # 4

# break
num = [1, 3, 4, 2, 5, -1, 0, 2, 4]
count = 0
for i in num:
    if i < 0:
        break
    else:
        count += i
    
print(count) #>> 15

# continue
num = [1, 3, 4, 2, 5, -5, 0, 2, 4]
count = 0
for i in num:
    if i < 0:
        continue
    count += i
    
print(count) #>> 21

# remove element (method - search through a copy of the list.)
names = ['Haraka', 'Antutu', 'Winterfell', 'Risasi', 'Rubi', 'JS', 'Python']

for i in names[:]:
    if i not in ['Haraka', 'Risasi']:
        names.remove(i)

print(names) #>> ['Haraka', 'Risasi']

# else
# Any code in the else block will be executed if the for loop does not reach 
# the break command.
num = [1, 3, 4, 2, 5, 5, 0, 2, 4]
positive = False

for i in num:
    if i < 0:
        break
else:
    positive = True

print(positive) # True

# while
# Typically, if you have an object that supports brute force, for
# Iterate over the elements using a for loop. 
# While loops are used 
# In the absence of easy access to an object that supports brute force.

n = 3
while n > 0:
    print(n)
    n -= 1
    # >> 
    # 3
    # 2
    # 1

n = 3
while True:
    print(n)
    n -= 1
    if n == 0:
        break
    # 3
    # 2
    # 1