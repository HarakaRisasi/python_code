#_*_coding:utf-8_*_
#this one is like your scripts with argv
#*args - взять все аргументы функции и использовать их как список
def print_two(*args)
    #a & b - arguments
    a, b = args
    c = a + b
    print ("arg1: {0}, arg2: {1}". format(a, b))
    print ("A + B = {0}". format(c))

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: {0}, arg2: {1}". format(arg1, arg2))

#this just takes one argument
def print_one(arg1):
    print ("arg1: {0}". format(arg1))

#this one takes no arguments
def print_none():
    print ("I got nothing")

print_two (input("> name one: "), input("> name two: "))
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()