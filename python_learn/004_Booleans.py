# Python has a type bool which can take on one of two values: True and False.
#-------------------------------
x = True
print(x) #>> True
print(type(x)) #>> <class 'bool'>
#-------------------------------
#-------------------------------
# Comparison Operations
# Operation	Description		          Operation Description
# a == b	a equal to b              a != b	a not equal to b
# a < b	    a less than b	          a > b	    a greater than b
# a <= b	a less than or equal to b a >= b	a greater than or equal to b
#-------------------------------
#-------------------------------
def can_run_for_president(age):
    return age >= 35

print('can run 19 for president is', can_run_for_president(19)) #>> False
print('can run 45 for president is', can_run_for_president(45)) #>> True
#-------------------------------
#-------------------------------
print(3.0 == 3) #>> True
print('3' == 3) #>> False
#-------------------------------
#-------------------------------
def is_odd(n):
    return(n % 2) == 1

print("Is 100 odd?", is_odd(100)) #>> False
print("Is 1 odd?", is_odd(1)) #>> True
print("Is -11 odd?", is_odd(-11)) #>> True
#-------------------------------
#-------------------------------
# Combining Boolean Values
def can_run_for_president(age, is_natural_born_citizen):
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True)) #>> False
print(can_run_for_president(19, False)) #>> False
print(can_run_for_president(36, True)) #>> True
#-------------------------------