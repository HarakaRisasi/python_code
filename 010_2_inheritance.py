# Может случиться, что, пытаясь решить какую-то задачу, вы обнаружите, что уже
# существует класс, создающий объекты, которые делают почти все из того, что нужно.
# Избавляет от проблем
# - модификации старого класса (ненужные усложнения)
# - копирования класса с дополнением новыми методами(усложнение в обслуживании)
# Наследование - это создание нового класса из уже существующего, который при этом
#   содержит какието дополнения и изменения.
#   (отличный способ использовать код повторно)
# Термины ООП:
# Оригинальный класс называется 
# - предком, 
# - суперклассом 
# - или базовым классом, 
# Новый класс называется
# - потомком, 
# - подклассом 
# - или классом-наследником.

class Car():
    pass
class Ferrari(Car):
    pass

# maked objects by each class
give_me_a_car = Car()
give_me_a_ferrari = Ferrari()
# Объект с именем give_me_a_ferrari является экземпляром класса Ferrari, 
# но он также наследует все то, что может делать класс Car.

# Extend the class by method(name'exclaim')
class Car():
    def exclaim(self):
        print('I\'am a Car!')

class Ferrari(Car):
    pass

give_me_a_car = Car()
give_me_a_ferrari = Ferrari()

give_me_a_car.exclaim() #>> I'am a Car!
give_me_a_ferrari.exclaim() #>> I'am a Car!
# класс Ferrari унаследовал метод exclaim() класса Car

# Operator Overloading
# modify_method_exclaim()_for_Ferrari_class
class Car():
    def exclaim(self):
        print('I\'m a car!')

class Ferrari(Car):
    def exclaim(self):
        print('I\'m a car! But more, i\'m a Ferrari.')

give_me_a_car = Car()
give_me_a_car.exclaim() #>> I'm a car!

give_me_a_ferrari = Ferrari() #>> I'm a car! But more, i'm a Ferrari.
give_me_a_ferrari.exclaim()

# The new Person class
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ' Esquire'

person = Person('Haraka')
doctor = MDPerson('Risasi') 
lawyer = JDPerson('Sherlock')

print(person.name) #>> Haraka
print(doctor.name) #>> Doctor Risasi
print(lawyer.name) #>> Sherlock Esquire

# Adding_Method_into_kid_class
class Car():
    def exclaim(self):
        print('I\'am a car!')

class Ferrari(Car):
    def exclaim(self):
        print('I\'m a car! But more, i\'m a Ferrari.')
    def need_a_push(self):
        print('A little help here?')

# maked_class_object
give_me_a_car = Car()
give_me_a_ferrari = Ferrari()

# call_method_of_class
give_me_a_ferrari.need_a_push() #>> A little help here?
give_me_a_ferrari.exclaim() #>> I'm a car! But more, i'm a Ferrari.