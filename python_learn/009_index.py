# Python slices

# # access to the last element

#  [0][1][2][3][4][5]
# ' H  a  r  a  k  a '
#  -6 -5 -4 -3 -2 -1

# При определении среза с двоеточием ( : ) первый индекс не является
# обязательным. Если первый индекс не указан, то срез по умолчанию начинается
#  с первого элемента списка (нулевой элемент)
import os
os.system('cls' if os.name == 'nt' else 'clear')

my_num = [1, 2, 3, 4, 5, 6]
print(my_num[-1]) #>> 6
print(my_num[-2]) #>> 5
print(my_num[-3]) #>> 4

my_str = 'Haraka'
print(my_str[-1]) #>> a

my_tupl = ('Haraka', 23, 'Senior')
print(my_tupl[-1]) #>> Senior

my_list = ['Haraka', 'Risasi', 'Coder']
print(my_list[:2]) #>> ['Haraka', 'Risasi']
print(my_list[-2:]) #>> ['Risasi', 'Coder']

my_str = 'Risasi'
print(my_str[2:]) #>> sasi
print(my_str[:2]) #>> Ri
print(my_str[-4:]) #>> sasi

my_list = ['New', 'List', 'Copy']
print(my_list[:]) #>> ['New', 'List', 'Copy']

# Если оба индекса отсутствуют, то возвращаемый срез проходит 
# от начала до конца (и содержит копию списка). Эта конструкция может 
# использоваться для быстрого копирования списков

# python slicer increments
my_list = [1, 2, 3, 4, 5, 6, 'dog', 7]
print(my_list[::2]) #>> [1, 3, 5, 'dog']
print(my_list[1:5:2]) #>> [2, 4]
print(my_list[::-1]) #>> [7, 'dog', 6, 5, 4, 3, 2, 1]
print(my_list[::-2]) #>> [7, 6, 4, 2]
print(my_list[5:0:-2]) #>> [6, 4, 2]

my_str = 'Risasi'
print(my_str[::-1]) #>> isasiR
print(my_str[5:0:-2]) #>> iai

# Операции индексирования используются для извлечения 
# отдельных значений из последовательностей.