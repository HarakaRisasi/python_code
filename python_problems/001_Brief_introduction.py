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
class Person:
    def __init__(self):
        pass

# single_level_inheritance
class Employee(Person):
    def __init__(self):
        pass

# multi-level inheritance
class Manager(Employee):
    def __init__(self):
        pass

# Multiple inheritance
class Enterprenaur(Person, Employee):
    def __init__(self):
        pass