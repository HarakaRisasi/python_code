#_*_coding:utf-8_*_

from sys import argv

script, input_file = argv

#.read - возвращает указанное кол-во байтов из файла
#   f = open('text.txt')
#   print(f.read(2))

def print_all(f):
    print f.read()

#seek(искать) - устанавливае текущую позицию файла
#   test.txt contents:
#       ABCDE
#   f = open(test.txt)
#   f.seek(3)
#   f.read()
#       DE

#Когда вы открываете файл, система указывает на начало файла. 
#Любое чтение или запись, которые вы делаете, 
#будут происходить с самого начала. 
#Операция seek() перемещает этот указатель на какую-либо 
#другую часть файла, чтобы вы могли читать или писать в этом месте.

#Итак, если вы хотите прочитать весь файл, 
#но пропустите первые 20 байтов, откройте файл, 
#найдите (20), чтобы перейти туда, где вы хотите начать чтение, 
#а затем продолжайте чтение файла.

#Или скажите, что вы хотите читать каждый 10-й байт, 
#вы можете написать цикл, который ищет (9, 1) 
#(перемещает 9 байт вперед относительно текущих позиций), 
#читает один байт, повторяется.

def rewind(f):
    f.seek(3)

#.readline() - считывает из файла одну строку и возвращ. ее.

#example - исп. Понадобилось из кучи файлов 
#(около 200 000) прочитать 6 и 9 строку

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print"Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
