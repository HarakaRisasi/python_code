#_*_coding:utf-8_*_
my_name = "Aleksandr V. Andriyanov"
my_age = 28 #not a lie
my_height = 179 #centimetre
my_weight = 153 #lbs
my_eyes = "Green"
my_teeth = "White"
my_hair = "Brown"

#ФОРМАТИРОВАНИЕ СТРОК
#%s(string) - вставить значение переменной строкового типа
#%d(decimal) - вставить значение переменной числового типа
#%f(float) - то же, что и числа, но с точкой
#%r(representation) - вставить значение любого типа.

#!!!%r - используется для дебага кода, поскольку он отображает
#        поскольку он отображает необработанные данные переменной
#!!!НО %s и %... используются для отображения данных пользователю.


print "Let's talk about %s." %my_name
print "He's %d centimetres tall." %my_height
print "He's %d pounds heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." %my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)

one = "hello"
two = 21
three = "world"
four = 4.3

print "%r If you see this, then %r and %r, is your %r" %(
        one, two, four, three)
