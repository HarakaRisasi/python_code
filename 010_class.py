# A class is a blueprint for objects
# one class for any number of objects of that type.
# Also call it an abstract data type.
# Interestingly, it contains no values itself, 
# but it is like a prototype for objects.

# Многие объектно-ориентированные языки, такие как C++,
# Java и Python, используют классы для определения состояния, которое
# может храниться в объекте, и методов для изменения этого состояния.

# Если классы являются определениями состояния и методов, экземпляры
# являются воплощениями этих классов. Как правило, когда разработчик
# говорит об объектах, он имеет в виду экземпляры классов.

# Чтобы создать экземпляр класса str с именем b , используйте синтаксис
# строковых литералов Python:
b = 'I\'m a string'
print(b) #>> I'm a string
# Термин «литерал» в данном случае означает специальный синтаксис
# создания строк, встроенный в Python.

# Если программисты начнут обсуждать b , вы можете услышать самые
# разные термины. 
# « b — это строка», 
# « b — это объект», 
# « b — это экземпляр строки»

# Прежде всего заметим, что классы не всегда необходимы в Python. 
# Подумайте, нужно ли определять класс или же хватит функции (или группы функций).

# Класс может быть полезен для программного представления
# физических или концептуальных объектов. 
# Понятия, являющиеся описаниями, — скорость, температура, среднее арифметическое, цвет
# — не являются хорошими кандидатами для классов.

# Если вы решили, что хотите моделировать что-либо с помощью класса,задайте себе следующие вопросы:
# У него есть имя?
#   Имена классов записываются в «верблюжьем регистре»
# Какими свойствами он обладает?
# Присущи ли эти свойства всем экземплярам класса? 
#   А именно:
#       Какие свойства являются общими для класса в целом?
#       Какие из этих свойств уникальны для каждого экземпляра?
#       Какие операции он выполняет?

num = 42
answer = str(num)
print(answer) #>> 42
print(type(answer)) #>> <class 'str'>

# class "Chair"
# Есть ли имя у моделируемой сущности? Да, «кресло». 
# Среди свойств
# кресла можно выделить номер, вместимость, наличие планки безопасности и мягких сидений. 
# Если погрузиться немного глубже, 
# вместимость можно разбить на максимальную вместимость и текущую занятость.
# Максимальная емкость должна оставаться постоянной, 
# тогда как занятость может изменяться в любой момент времени.

# Строки документации - строковые литералы, 
# которые являются первым оператором в модуле, функции, классе или определении метода.

# Создать класс:
# Определяете нужные атрибуты. 
#   Те атрибуты, которые существуют на уровне класса, размещаются в определении класса. 
#   Атрибуты, уникальные для каждого экземпляра, размещаются в конструкторе.
# Также можете определить методы с операциями, изменяющими экземпляр класса.

# Методы также определяются на уровне класса, но атрибуты экземпляров — нет. 
# Так как атрибуты экземпляров уникальны для объекта, они хранятся в экземпляре.

class Chair:                            # name
    ''' A chair on a  chairlift '''     # documentation line
    max_occupants = 4                   # atributes of a class (4 occupants)

    def __init__(self, id):             # method(constructor)
        self.id = id                    # inside constructor body, add two atributes 'id', 'count'
        self.count = 0
    
    def load(self, number):             # method 'load'.
        self.count += number            # this method represents an operation that can be performed 
                                        # by an instance of a class.             
    def unload(self, number):
        self.count -= number

print(Chair.__doc__) #>> 'A chair on a  chairlift'

# Атрибут класса используется для хранения состояния, общего для всех экземпляров класса.

# Функция, определяемая прямо в теле класса, называется методом.

# Так как этот метод имеет специальное имя __init__ , он называется конструктором.
# Конструктор вызывается при создании экземпляра класса.

# Метод получает два параметра, self и id . 
# У большинства методов первым параметром является self. 

# Его можно интерпретировать как экземпляр класса.

# Конструктор вызывается при создании экземпляра класса.

# В Python есть встроенная функция id , но вы также можете использовать
# это имя как имя атрибута класса.

# Если экземпляру было присвоено имя chair , то для получения значения id 
# следует использовать запись chair.id . Таким образом,

# Методы представляют собой функции, присоединенные к классу. 
# Метод вызывается не сам по себе, а для конкретного экземпляра класса:
# 'matt'.capitalize() #>> 'Matt 
# встроенная функция не замещается.

class Try:
    def mymethod(self):
        print("Hello")
        print("Hi")
        

# create 'obj1' object for 'try1()' class.
obj1 = Try()
# called the method 'method()'.
# a method may take arguments.
obj1.mymethod() 
#>> 
# Hello
# Hi

class FruitOne:
    def size(self, x):
        print(f'I\'m size {x}')

orange = FruitOne()
orange.size(7) 
#>> I'm size 7

class FruitTwo:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def salutation(self):
        print(f'I\'m {self.color} and a size {self.size}')

orange = FruitTwo('Orange', 7)
orange.salutation() 
#>> I'm Orange and a size 7

# bank account class
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        # return self.balance
        print(f'Withdrawal of -{amount} RUB from an account, balance your account = {self.balance} RUB')
    
    def deposit(self, amount):
        self.balance +=  amount
        # return self.balance
        print(f'Depositing funds of +{amount} RUB, balance your account = {self.balance} RUB')
    
a = BankAccount()
b = BankAccount()

a.deposit(100000) #>> Depositing funds of +100000 RUB, balance your account = 100000 RUB
a.withdraw(12546) #>> Withdrawal of -12546 RUB from an account, balance your account = 87454 RUB

b.deposit(6584) #>> Depositing funds of +6584 RUB, balance your account = 6584 RUB
b.withdraw(17) #>> Withdrawal of -17 RUB from an account, balance your account = 6567 RUB

# Классы и обьекты(как можно проще)

# Объект

# Объект содержит как данные (переменные, которые называются атрибутами,
# так и код (функции, которые называются методами).
# Строки 'cat' и 'duck'
# также являются объектами и имеют методы, например, capitalize() и replace().
print('cat'.capitalize()) #>> Cat
print('duck'.replace('d', 'c')) #>> cuck

# При создании нового объекта, которые не создавал никто, 
# надо создать класс, который демонстрирует его содержимое.
# ! Объекты можно считать существительными, а их методы — глаголами.
# Объект представляет отдельную вещь, а его методы определяют, 
# как она взаимодействует с другими вещами.

# Класс
# Если Объект это коробка - то Класс это форма из которой эта коробка создается 
# ex: String - это встроенный класс Python который создает строковые объекты вроде 'cat', 'duck'

# ex: определять объекты представляющие информацию о людях.
#     Каждый объект будет представлять одного человека.
#     Сначала нужно определить класс Person в качестве формы.
class Person:
    pass

# Такое определение является необходимым минимумом создания объекта. 
# объект создается из класса с помощью вызова имени класса так, будто оно является функцией:

someone = Person()

# В этом случае Person() создает отдельный объект класса Person 
# и присваивает его имени someone.

class Person:
    def __init__(self): # специальный метод инициализации
        pass
# __init__() — это особое имя метода, 
# который инициализирует отдельный объект с помощью определения его класса
# Аргумент self указывает на сам объект.

class Person:
    def __init__(self, name):
        self.name = name

donald = Person('Duck')

print(f'The Donald is {donald.name}') # The Donald is Duck

# - этот объект похож на любой другой объект Python. 
# - можно использовать его как элемент списка, кортежа, словаря или множества. 
# - Можно передать его в функцию как аргумент или вернуть его в качестве результата.

# ! Помни, внутри определения класса Person получаешь доступ к атрибуту name
#   с помощью конструкции self.name . 
#   Когда создаете реальный объект вроде donald , то ссылаетесь на этот атрибут как donald.name.

# ! Не обязательно иметь метод __init__ в описании каждого класса, он используется для того, 
#   чтобы различать объекты одного класса.