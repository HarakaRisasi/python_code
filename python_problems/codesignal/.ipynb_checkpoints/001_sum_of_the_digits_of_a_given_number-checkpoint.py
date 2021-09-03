
def addTwoDigits(n):
    ''' Convert int 'n' to str, then use lambda function to convert back to int and get sum of all elements  '''
    n = str(n)
    return sum([int(i) for i in n])
    
print(addTwoDigits(48))
#----------------------------------------
# Get first and back digits of number n // 10 + n % 10
print(29 // 10) # 2
print(29 % 10) # 9