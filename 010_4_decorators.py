# Еще один способ определить свойства — это декораторы. 
# В следующем примере мы определим два разных метода с именем name(), 
# предшествовать которым будут разные декораторы:
# @property , который размещается перед геттером;
# @name.setter , который размещается перед сеттером.

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    # устанавливаем значение атрибутов с помощью свойств
    def diameter(self):
        return self.radius * 2

c = Circle(5) # make object 'c' from class Circle
print(c.diameter)
#>> 10

c.radius = 7 # assigned a new value inside to the method __init__ 
             # or attribute of class 'Circle'
print(c.diameter)
#>> 14

# Name Distortion for Security
# Python предлагает соглашения по именованию для атрибутов, 
# которые не должны быть видимы за пределами определения их классов: 
# имена начинаются с двух нижних подчеркиваний ( __ ).

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.__name = input_name

fowl = Duck('Howard')
print(fowl.name) 
#>>
# inside getter
# Howard

fowl.name = 'Donald'
# inside setter

print(fowl.name)
#>>
# inside getter
# Donald


# Вы не можете получить доступ к атрибуту __name :
#fowl.__name #>> Error

# !BUT
fowl._Duck__name #>> Donald