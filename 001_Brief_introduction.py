# 000_all
# The Python for Loop
# for <var> in <iterable>:
#     <statement(s)>
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
#=> foo
#=> bar
#=> baz

# Hello, Python!
spam_amount = 0
spam_amount += 4

# The colon (:) at the end of the if line indicates 
# that a new "code block" is starting.
if spam_amount > 0:
    print('But I don\'t want ANY spam!')

viking_song = 'Spam Spam Spam'
print(viking_song)

print(spam_amount)

# Numbers and arithmetic in Python
# Operator	Name	        Description                                    Example
# a + b	    Addition	    Sum of a and b                                 5 + 2 = 7
# a - b	    Subtraction	    Difference of a and b                          5 - 2 = 3
# a * b	    Multiplication	Product of a and b                             5 * 2 = 10
# a / b	    True division	Quotient of a and b                            5 / 2 = 2.5
# a // b	Floor division	Quotient of a and b, removing fractional parts 5 // 2 = 2
# a % b	    Modulus	        Integer remainder after division of a by b     5 % 2 = 1
# a ** b	Exponentiation	a raised to the power of b                     5 ** 2 = 25
# -a	    Negation	    The negative of a                              -5

# Order of operations
hat_height_cm = 25
my_height_cm = 189
# how tall am I, in meters, when wearing my hat?
total_height_maters = (hat_height_cm + my_height_cm) / 100

print('Height in meters =', total_height_maters, '?') #=> Height in meters = 26.89 ?

# Builtin functions for working with numbers
# min and max
print(min(1, 2, 3)) #=> 1
print(max(1, 2, 3)) #=> 3

# abs
print(abs(32)) #=> 32
print(abs(-32)) #=> 32

# int and float can also be called as functions which convert 
# their arguments to the corresponding type:
print(float(10)) #=> 10.0
print(int(3.33)) #=> 3
print(int('909')) #=> 909
print(int('909') + 1) #=> 910 

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

# Создайте класс с именем Person, используйте функцию __init __ (), 
# чтобы назначить значения для имени и возраста:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Объекты также могут содержать методы. Методы в объектах - это функции, которые принадлежат объекту. 
    def get_name(self):
        return self.name
    # В объектно-ориентированном программировании 'конструктором класса' называют метод, 
    # который автоматически вызывается при создании объектов. 
    
    # Метод конструктора используется для инициализации данных. 
    # Он запускается, как только создается экземпляр объекта класса. 
    
    # В Python наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том, 
    # что он принадлежит к группе методов перегрузки операторов. 
    
    # Используйте функцию __init __ () для присвоения значений свойствам объекта или другим операциям, 
    # которые необходимо выполнить при создании объекта:
    
    # Обязательно это Первый параметр любой функции в классе – self 
    # – ссылка на сам только что созданный объект.
    # Параметр self является ссылкой на текущий экземпляр класса 
    # и используется для доступа к переменным, принадлежащим классу.

# Вот как создать объект Person
p = Person('Alice', 22)

print(p.age, p.name) #=> 22 Alice

# Object Methods
print(p.get_name()) #=> Alice

# 007_OOP_conceptions
# Encapsulation
#   Data can be encapsulated such that it is invisible to the “outside world”
#   Data can only be accessed via methods.
#   
#   procedural              class
#                           -------------
#   Data                    -Data       -
#   Function                -Function   -
#   Function                -Function   -
#   Function                -Function   -
#                           -------------
# Polymorphism 
# is the ability of one object to be treated and used like another object. 
# For example, we treat duck as an animal and not just as a duck. 
# Similarly we treat dog and cat also as animals.
# 
# Inheritance
# Inheritance is an “is-a” relation, which inherits the attributes and behaviors from its parent class. 
# For example, dog is an animal. It means animal is a parent class and Dog is the child class. 
# The child class “Dog” inherits the attributes like age and weight from the parent class , which is an animal. 
# The inheritance allows the child class to inherit the attributes and behaviors of its parent.

# 008_class_and_object
# Class is a blueprint of the real-life entity.
# Class - проект, созданный программистом для объекта. 
# Это определяет набор атрибутов, которые будут характеризовать любой объект, 
# который создается из этого класса.
class Shark:
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")

# Object — Объект является экземпляром класса.
# Методы - это особый вид функций, определенных в классе.
# Аргументом для этих функций является слово self, которое является ссылкой на объекты, созданные на основе этого класса.

# Мы можем взять класс Shark, определенный выше, и использовать его для создания объекта или его экземпляра.
# Мы сделаем объект класса Shark с именем sammy:
sammy = Shark()
# Здесь мы инициализировали объект sammy, как экземпляр класса, установив его равным Shark().

# Воспользуемся двумя методами для объекта класса Shark, sammy:
sammy.be_awesome() #=> The shark is being awesome.
sammy.swim() #=> The shark is swimming.

# 009_more_about_inheritance
# As the name suggest, this concept is about inheriting properties from an existing entity. 
# Inheritance is when a class uses code constructed within another class. 
# Classes called child classes or subclasses inherit methods and variables from parent classes or base classes.
# class Person:
#     def __init__(self):
#         pass

# single_level_inheritance
# class Employee(Person):
#     def __init__(self):
#         pass

# multi-level inheritance
# class Manager(Employee):
#     def __init__(self):
#        pass

# Multiple inheritance
# class Enterprenaur(Person, Employee):
#     def __init__(self):
#         pass

# inherited parameters of class
class Shark_mini:
    animal_type = "fish"
    location = "ocean"
    followers = 5

new_shark = Shark_mini()


print(new_shark.animal_type, new_shark.location, new_shark.followers + 1) #=> fish ocean 6

# Parent or base classes create a pattern out of which child or subclasses can be based on. 
# Parent classes allow us to create child classes through 
#  inheritance without having to write the same code over again each time. 
# Any class can be made into a parent class, so they are each fully functional
#  classes in their own right, rather than just templates.

# class
#  class Fish:
#      # method
#     def __init__(self, first_name, last_name = "Fish")
#         # attributes
#         self.first_name = first_name
#         self.last_name = last_name
#         self.skeleton = skeleton
#         self.eyelids = eyelids
# 
# def swim(self):
#     print("The fish is swimming.")
#
# def swim_backwards(self):
#     print("The fish can swim backwards.")#

# Child or subclasses are classes that will inherit from the parent class. 
# That means that each child class will be able to make use 
#   of the methods and variables of the parent class.

# class Trout(Fish):
#     pass # так же удобно справа от pass писать комментарий, если планируется что - то в данной строке.
# Pass - Оператор-заглушка, равноценный отсутствию операции.
# В ходе исполнения данного оператора ничего не происходит, поэтому он может использоваться 
# в качестве заглушки в тех местах, где это синтаксически необходимо, например: в инструкциях, 
# где тело является обязательным, таких как def, except и пр.