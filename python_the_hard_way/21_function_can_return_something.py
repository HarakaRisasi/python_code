#_*_coding:utf-8_*_
def add(a, b):
    print ("ADDING {0} + {1}". format(a, b))
    return a + b

def substract(a, b):
    print ("SUBSTRACTING {0} - {1}". format(a, b))
    return a - b

def multiply(a, b):
    print ("MULTIPLYING {0} * {1}". format(a, b))
    return a * b

def devide(a, b):
    print( "DEVIDING {0} / {1}". format(a, b))
    return a / b

print ("Let's do some math with just function!")

age = add(30 , 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print ("Age: {0}\nHeight: {1}\nWeight: {2}\nIQ: {3}". format(age, height, weight,iq))

#A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, devide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")