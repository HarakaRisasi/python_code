# Find the sum of all the multiples of 3 or 5 below 1000

import subprocess
subprocess.call("clear")

def mult_three_and_five(num):
    natural = [] # creating a dynamic array
    i = 1 # start of calculation
    while i < num:
        if i % 3  == 0 or i % 5 == 0:
            natural.append(i) # adding the element into list
        i += 1
    return sum(natural) # sum of all elements of array

print(mult_three_and_five(1000)) #>> 233168