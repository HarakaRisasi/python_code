##_*_ coding: utf-8 _*_

from __future__ import print_function
import sys, os, time

#for in - для перебора элементов любого указанного списка
#for ..element.. in ..list name.. :
#Список
chars = [ 'A', 'B', 'C' ]
#Кортеж
fruits = ( 'Apple', 'Banana', 'Cherry' )
#Словарь
dict = {'name':'Alex', 'ref':'Python', 'sys':'Linux'}

#item - элемент списка
#   a = [1,2,3,4,5]
#для элемента в списке 'а'
#   for item in a :
#       print( item, end = ' ')


print( '\nElements:\t', end = ' ' )
for item in chars :
    #end = ' ' - это то, что я хочу напечатать после выполнения print
      print( item, end = ' ' )

print( '\nElements:\t', end = ' ' )
#Для элементов в нумерованном списке chars
for item in enumerate( chars ) :
    print( item, end = ' ' )

#zip - функция, что берет на вход несколько списков
#и создает из них zip объект - список кортежей
#перечисляющий элементы списков
#a = [1,2,3]
#b = ['Alpha', 'Betta', 'Gamma']
#for item in zip( a, b ) :
#   print( item, end = '\n' )
#Output:
#1, Alpha
#2, Betta
#3, Gamma

print( '\nZipped:\t', end = ' ' )
for item in zip( chars, fruits ) :
    print( item, end = ' ' )

#Словарь(dict)-неупорядоченные коллекции произвольных объектов
#              с доступом по ключу.(Ассоциативные массивы, 
#              хэш-таблицы.

print( '\nPaired:' )
for key, value in dict.items() :
    print(key, '=', value )

print( '\n' )

#Этот цикл проходится по любому итерируемому объекту(строке или      #списку) и во время прохода выполняет тело цикла
for i in 'hello world' : 
    print(i * 2, end = ' ')
print( '\n' )
