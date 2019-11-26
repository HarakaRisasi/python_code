# Reversing a List
list_0 = [12, 9.25, 89, 3.02, -75.23, -7.2, 6.3]
list_0.reverse()
print(list_0) #=> [6.3, -7.2, -75.23, 3.02, 89, 9.25, 12]

# Print list elements in any order
list_1 = [1, 2, 3]
x, y, z = list_1
print(z, y, x) #=> 3, 2, 1
print(y, z, x) #=> 2, 3, 1

# Using Generators Inside Functions
print(sum(i for i in range(10))) #=> 45

# Using the zip() function
year = (1989, 1990, 1991, 1992)
month = ('NOV', 'DEC', 'JAN', 'FAB')
day = (13, 14, 15, 16)

print(list(zip(day, month, year))) #=> [(13, 'NOV', 1989), (14, 'DEC', 1990), (15, 'JAN', 1991), (16, 'FAB', 1992)]

for m, d, y  in zip(month, day, year):
    print(d, m, y)
    #=> 13 NOV 1989
    #=> 14 DEC 1990
    #=> 15 JAN 1991
    #=> 16 FAB 1992

# Swap two numbers using a single line of code
x, y = 13, 14

print (x, y) #=> 13 14

x, y = y, x

print(x, y) #=> 14 13

# Transpose a Matrix
# Transposing a matrix involves converting columns into rows.
x = [
    [13, 21],
    [24, 30],
    [35, 40]
    ]
transponsed = zip(*x)
print(list(transponsed)) #=> [(13, 24, 35), (21, 30, 40)]

# Print a string N Times
s = 'Point'
print((s + ' ') * 3) #=> Point Point Point 

# List slicing
l = range (10)
print(l[:: 2]) #=> range(0, 10, 2) or [0, 2, 4, 6, 8]

l = [1, 2, 4, 3, 5, 6]
print(l[::-1]) #=> [6, 5, 3, 4, 2, 1]

l = 'abcd'
print(l[:: 2]) #=> 'ac'
print(l[:: -1]) #=> 'dcba'

# Find the Factors of a Number
f = 15
print('The factors of ', f, 'are: ')
for i in range(2, f): # range from 2 to 15 without 1 and 15
    if (f % i == 0):
        print(i)
        #=>
        # The factors of  15 are: 
        # 3
        # 5

# Checking the Usage of Memory
# Return the size of an object in bytes. 
import sys # System-specific parameters and functions (sys)
a, b, c, d, e, f, g, h, i = 'a', 'ac', 'alphabet', 1, 10, 100, 1.0, 1.9, 1.99
print(sys.getsizeof(a)) #=> 50
print(sys.getsizeof(b)) #=> 51
print(sys.getsizeof(c)) #=> 57
print(sys.getsizeof(d)) #=> 28
print(sys.getsizeof(e)) #=> 28
print(sys.getsizeof(f)) #=> 28
print(sys.getsizeof(g)) #=> 24
print(sys.getsizeof(h)) #=> 24
print(sys.getsizeof(i)) #=> 24