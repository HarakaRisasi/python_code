# 001_variables
msg = "Hello World!"
print(msg); #=> Hello World!

# 002_Type_of_data
# Must_learn_these_data_types:
#-----------------------------
# String
#-----------------------------
# Integer
#-----------------------------
# Float numbers
#-----------------------------
# Boolean
#----------------------------- 
# Array
# Список (list) в Python обозначается так:  
# lst = ['spam', 'drums', 100, 1234]
#-----------------------------
# Tuple
# Кортеж (tuple) - это тоже список, только с неизменяемыми элементами, 
# обозначается так: 
# mytuple = (1, 2, 3) 
# Разложить список или кортеж по переменным можно так:
# mytuple = (1, 2, 3)
# a, b, c = mytuple
# Обратиться к элементу списка или кортежа можно с помощью квадратных скобок. 
# Счет с нуля:
# mytuple = (1, 2, 3)
# a = mytuple[2] 
# print(a) #=> 3
#-----------------------------
# Hush
# ("Map" или "ассоциативный массив")
# Словарь (hash, хэш, предопределенный массив) – изменяемая структура данных, 
# предназначенная для хранения элементов вида ключ: значение.
# Создаем хеши:
# >>> h1 = {1:"one", 2:"two", 3:"three"}
# >>> h2 = {0:"zero", 5:"five"}
# >>> h3 = {"z":1, "y":2, "x":3}
#-----------------------------

# 003_operations
# arithmetic_operation
x = 5 + 2
print(x) #=> 7

# comparison_operation
y = 3 > 4
print(y) #=> false

# logic operation
z = True or False
print(z) #=> True

# 004_condition
#if, else, if elif else.
if 3 > 5:
    print('3 is greater than 5')
else:
    print('3 is less than 5')
#=> '3 is less than 5'

# 005_function
def say_hello(msg):
    # this is the function
    # msg is the input parameter
    print('hello %s' % (msg)) # for python -V 2.+
    #=> 'hello world'
    print(f"hello {msg}") # for python -V 3.6+
    #=> 'hello world'
    
# F-Строки: Новый улучшенный способ форматирования строк в Python
# 'форматированные строковые литералы', f-strings являются строковыми литералами 
# с «f or F» в начале и фигурные скобки, содержащие выражения, которые в дальнейшем будут заменены своими значениями.

# calling the say_hello function
say_hello('world') #=> hello world

# 006_OOP
# An object has:
   # identity (a unique reference)
   #    social security number (cpr), employee number, passport number
   # state, also called characteristics (variables)
   #     hungry, sad, drunk, running, alive
   # behavior (methods)
   #     eat, drink, wave, smile, kiss

# Одна из самых популярных парадигм программирования называется объектно-ориентированным программированием (ООП).
# В объектно-ориентированном программировании  объект  относится к конкретному экземпляру  класса .
# А класс - это как план состояния и действий которые может выполнить объект.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    # В объектно-ориентированном программировании 'конструктором класса' называют метод, 
    # который автоматически вызывается при создании объектов. 
    # В Python наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том, 
    # что он принадлежит к группе методов перегрузки операторов. 
    # Первый его параметр – self – ссылка на сам только что созданный объект.

# Вот как создать объект Person
p = Person('Alice', 22)
p.get_name() #=> 'Alice'

#007_OOP_conceptions


