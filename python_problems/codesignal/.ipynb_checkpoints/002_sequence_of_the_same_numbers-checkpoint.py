
def largestNumber(n):
    ''' The maximum number formed into a sequence of the same numbers whose length is determined by the input number '''
    x = [] # we're make empty array

    # We're fill the array with nines
    for n in (range(n)):
        x.append(9)
    
    # Convert each value of list to string
    n = [str(i) for i in x]
    
    # Convert to int. of each value of list and join of each value to single number
    n = int(''.join(n))

    return n

print(largestNumber(8))

#------------------------------------
def largestNumber_1(n):
    return int('9'*n)


