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

# класс-потомок может добавить или перегрузить(изменить) метод класса-предка.

# repeat(class andwhat is constructor)
# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

# - class – Here is a class named Person.
# - Constructors have the default name __init__. 
#   They are functions that are implicitly called when an object of 
#   the class is created.
# - All instance methods including the constructor 
#   have their first parameter as self.
# - self refers to instance that is being referenced while calling the method.
# - name and age are the instance variables.#

# test
class Dog():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)

print(f'{philo.name} is {philo.age} and {mikey.name} is {mikey.age}')
#>> Philo is 5 and Mikey is 6

# Is Philo a mammal?
if philo.species == 'mammal':
    print(f'{philo.name} is a {philo.species}!')
    #>> Philo is a mammal!


# метод super() - ecли нужно вызвать оригинальный метод родительского класса?
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        # Строка self.email = email 
        # — это новый код, который отличает класс EmailPerson от класса Person .

# Когда определяеся метод __init__() для своего класса, 
# происходит замена метода __init__() родительского класса,
# который больше не вызывается автоматически.
# - нужен не явный вызов родительского класса
# - Метод super() получает определение родительского класса Person.
# - Метод __init__() класса EmailPerson, вызывает метод __init__() класса Person.
# - Последний заботится о том, чтобы передать аргумент self суперклассу, 
#   поэтому вам нужно лишь передать опциональные аргументы.
#   В нашем случае единственным аргументом класса Person() будет name.
# - Строка self.email = email — это новый код, который отличает 
#   класс EmailPerson от класса Person.

bob = EmailPerson('Bob', 'bobhardy@gmail.com')
print(f'Client name: {bob.name}\ne-mail: {bob.email}')
#>>
# Client name: Bob
# e-mail: bobhardy@gmail.com

# Почему бы нам просто не определить новый класс так, как показано далее?
class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

haraka = Person('Haraka', 'haraka@gmail.com')

print(f'name: {haraka.name}\ne-mail: {haraka.email}')
#>> 
# name: Haraka
# e-mail: haraka@gmail.com

# Мы могли бы сделать это, 
# но в таком случае потеряли бы возможность применять наследование. 
# Мы использовали метод super(), чтобы создать объект, который работает примерно 
# так же, как и объект класса Person. 
# Есть и другое преимущество:
# если определение класса Person в будущем изменится, 
# с помощью метода super() мы сможем гарантировать, что атрибуты и методы, 
# которые класс EmailPerson наследует от класса Person, 
# отреагируют на изменения.
# Используйте метод super() , когда потомок делает что-то самостоятельно, 
# но ему все еще нужно что-то от предка (как и в реальной жизни).
