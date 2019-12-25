# Что такое геттеры и сеттеры?
# Следующее понятие из мира ООП,которое следует рассмотреть - это геттеры и сеттеры 
# (getter - от англ. "get" - получать, и setter - от англ. "set" - устанавливать). 
# Это общепринятый способ вводить данные ("set") или получать данные ("get"). 

# #>> Тут, нам стоит вспомнить про такой принцип ООП как инкапсуляция 
# (если Вы не знаете, что это такое, вернитесь назад и прочитайте статью 
# "Что такое ООП"). 

########################################################################
# С помощью геттеров и сеттеров 
# Вы защищаете содержимое программы - когда ей пользуется кто-то другой.
########################################################################

# Для управляемого доступа к состоянию объекта 
# используют специальные функции, так называемые «геттеры» и «сеттеры».

# Для лучшего контроля над свойством его делают приватным, 
# а запись значения осуществляется через специальный метод, 
# который называют «сеттер» (setter method).

# Для того, чтобы дать возможность внешнему коду узнать его значение, 
# создадим специальную функцию – «геттер» (getter method).

# Отдельные объектно-ориентированные языки поддерживают закрытые атрибуты
# объектов, к которым нельзя получить доступ непосредственно; 
# программистам зачастую приходится писать геттеры и сеттеры, 
# чтобы считать и записать значения таких атрибутов.

# В Python геттеры и сеттеры не нужны, 
# поскольку все атрибуты и методы являютсяоткрытыми.

# Если прямой доступ к атрибутам заставляет вас нервничать, 
# вы, конечно, можете написать геттеры и сеттеры.
# Но сделайте это более характерным для Python способом — используйте свойства.

# Объект содержит как данные (переменные, которые называются атрибутами,
# так и код (функции, которые называются методами).

# Мы не хотим, чтобы люди обращались к атрибуту напрямую, 
# поэтому определим два метода: геттер ( get_name() ) и сеттер ( set_name() ).

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    # getter
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    # setter
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)
    # property возвращает объект 
    # - копию входящего с реализацией getter setter deletter методами…

# Новые методы действуют как обычные геттеры и сеттеры до последней строки,
# где они указываются как свойства атрибута name . 
# - Первый аргумент функции property() — это геттер, 
# - Второй — это сеттер.

fowl = Duck('Howard')
print(fowl.name)
#>> 
# inside the getter
# Howard

# Вы можете вызвать метод get_name() непосредственно, как обычный геттер:
fowl.get_name()
#>> inside the getter

# при присваиваении значения атрибуту name , вызывается метод set_name():
fowl.name = 'Duffy'
#>> inside the setter
fowl.name
#>> inside the getter

# Метод set_name() вы также можете вызвать непосредственно:
fowl.set_name('Buffy')
#>> inside the setter

# Итог:
# Для большего контроля над присвоением и чтением значения вместо 
# свойства делают «функцию-геттер» и «функцию-сеттер», 
# геттер возвращает значение, сеттер – устанавливает.

# Если свойство предназначено только для чтения, 
# то может быть только геттер, только для записи – только сеттер.