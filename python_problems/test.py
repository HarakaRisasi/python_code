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
print(numpy.transponse(x))