#---------------------------
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(1, 10, 100), end=" ")
print(least_difference(1, 10, 10), end=" ")
print(least_difference(5, 6, 7))
#>> 9 0 1
#---------------------------

#---------------------------
print(1, 2, 3, sep = ' < ') #>> 1 < 2 < 3
#---------------------------

#---------------------------
def greet(who = 'World!!!'):
    print('Hello,', who)

greet() #>> Hello, World!!!
greet(who = 'Haraka') #>> Hello, Haraka
#---------------------------

#---------------------------
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

print(
    call(mult_by_five, 1), #>> 5
    squared_call(mult_by_five, 1) #>> 25
)

# Exercises
# round
def round_to_two_places(num):
    return round(num, 2)

print(round_to_two_places(3.14159)) #>> 3.14