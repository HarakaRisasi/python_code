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

###################################################################
# test
# Parent class
class Car:
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self. model}'
        return long_name
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
###################################################################

###################################################################
# Specific class
# Battery () - Отдельный класс созданный для подробного описания части объекта. 
# Его суть в том, чтобы разгрузить объем кода написанного для класса. 
# В данном случае класс описывающий объект 'Battery' будет содержать 
# важные только для себя атрибуты и тем самым перегружать код объекта 'ElectroCar'.
# Этот класс можно использовать в основном классе как атрибут.
# self.battery = Battery()

# Then we can use a instance as an attribute in the ElectricCar class:
class Battery:
    '''A simple attempt to model a battery for an electric car.'''
    
    def __init__(self, battery_size = int(input())):
        '''Initialize the battery\'s attributes.'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.battery_size} - kWh battery.')
    
    def get_range(self):
        '''Print a statement about the range this battery prosides.'''
        range = int(self.battery_size * 3.15)       
        print(f'This car can go about {range} miles on a {self.battery_size}% charge.')
###################################################################

###################################################################
# Child class
class ElectricCar(Car):
    '''Represent aspects of a car, specifie to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then nitialize attribetes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery() # add a new attribute from 'class Battery()'
    
    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.battery_size} -kWh battery.')
    
    def fill_gas_tank(self):
        '''Electric cars don\'t have gas tanks.'''
        print(f'This car doesn\'t need a gas tank!')

# When you use inheritance, you can make
# your child classes retain what you need and override anything
# you don’t need from the parent class.

# При моделировании чего-то из реального мира в коде вы можете обнаружить, 
# что добавляете все больше и больше деталей в класс. 
# Вы обнаружите, что у вас есть растущий список атрибутов и методов, 
# и что ваши файлы становятся длиннее. 
# В этих ситуациях вы можете распознать, что часть одного класса 
# может быть записана как отдельный класс. 
# Вы можете разбить свой большой класс на меньшие классы, которые работают вместе.

my_Jaguar = ElectricCar('Jaguar', 'E-type', 2019)
print(my_Jaguar.get_descriptive_name()) #>> 2019 Jaguar E-type

# Эта строка говорит Python 
my_Jaguar.battery.describe_battery() #>> This car has a 75 - kWh battery.
# - посмотреть на инстанс my_Jaguar,
# - найти атрибут battery
# - вызвать метод describe_battery()

# Это выглядит как большая дополнительная работа, 
# но теперь мы можем описать батарею настолько подробно, 
# насколько мы хотим, не загромождая класс ElectricCar.

# input battery level
my_Jaguar.battery.get_range()
#>> This car can go about 236 miles on a 75% charge.
###################################################################

# Modeling Real-World Objects
# Это подводит вас к интересному моменту вашего роста как программиста. 
# Когда вы боретесь с такими вопросами, 
# вы думаете на более высоком логическом уровне, 
# а не на уровне, ориентированном на синтаксис. 
# Вы думаете не о Python, а о том, как представить реальный мир в коде. 
# Когда вы достигнете этой точки, вы поймете, 
# что часто нет правильных или неправильных подходов 
# к моделированию реальных ситуаций. 
# Некоторые подходы более эффективны, чем другие, 
# но для нахождения наиболее эффективных представлений требуется практика. 
# Если ваш код работает так, как вы хотите, у вас все хорошо! 
# Не расстраивайтесь, если вы обнаружите, что разбираете свои классы 
# и переписываете их несколько раз, используя разные подходы. 
# В стремлении написать точный и эффективный код 
# каждый проходит через этот процесс.
###################################################################

###################################################################
# test(restaurant)
class Restaurant:
    # Параметр self представляет экземпляр ( Restaurant в данном случае).
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self. cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'{self.restaurant_name} Restaurant')
        print(f'Cuisine type: {self.cuisine_type}')
    
    def open_restaurant(self):
        print(f'We are Open! Welcome.')

# the 'restaurant' variable points to an object, that is, an instance.
restaurant = Restaurant('Harafood de Paris', 'Cajun Food')

# call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
#>> 
# Harafood de Paris Restaurant
# Cuisine type: Cajun Food
# We are Open! Welcome.

class IceCreamStand(Restaurant):
    def __init__(restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        #>>>> TO BE CONTINUED
        
###################################################################
# Анализ экземпляра
# Если у вас имеется экземпляр и вы хотите узнать его атрибуты, 
# есть несколько вариантов.
# «...возвращает упорядоченный по алфавиту список имен, включающий
# (некоторые) атрибуты заданного объекта, а также атрибуты, доступные из него».
print(dir(Restaurant))