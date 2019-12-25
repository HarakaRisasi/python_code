# Syntax, Variables, and Numbers

# 001
print("You've successfully run some Python code") #>> You've successfully run some Python code
print("Congratulations!") #>> Congratulations!
print("Hello Python & World!!!") #>> Hello Python & World!!!

# 002
# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)
color = 'blue' # >> blue


# 003
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter * 0.5

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * radius ** 2

print(area) #>> 7.0685775

# 004
########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
print(a, b) #>> [1, 2, 3] [3, 2, 1]
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.
a, b = b, a
print(a, b) #>> [3, 2, 1] [1, 2, 3]
######################################################################

# 005
# a) Add parentheses to the following expression so that it evaluates to 1.
print((5 - 3) // 2) #>> 1
# b) Add parentheses to the following expression so that it evaluates to 0
print(8 - 3 * 2 - (1 + 1)) #>> 0

# 006
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3
print(to_smash) #>> 1