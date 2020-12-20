#!/usr/bin/python
# -*- coding: utf-8 -*-

# commands to remember:
# close - закрывает файл. по типу save/close
# read - читает содержимое файла. можно присвоить как результат к пер.
# readline - читает только одну строку текстового файла.
# truncate - очищает файл.
# write(stuff) - записывает материал в файл.

# импортирует аттрибут argv из модуля sys

from sys import argv

# Создание переменных и присвоение им значения из консоли

(script, filename) = argv

# Вывод и форматирование текста

print ("We're going to erase {0}".format(filename))
print ("If you don't want that, hit CTRL-C (^C).")
print ('If you do want that, hit RETURN.')

# Ввод с клавиатуры
# input - вводит выражения поэтому если текст - то писать "text"

input('?')

# Вывод текста

print ('Opening the file...')

# Открыть файл в режиме write
#   и присвоить его контент переменной target

target = open(filename, 'w')

# Вывод текста

print ('Truncating the file. Goodbye!')

# Вызов переменной содержащей в себе контент файла и подключение
#   функции очистки

target.truncate()

# Вывод на экран

print ("Now I'm going to ask you for three lines.")

# Ввод данных и писвоение их к переменной

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

# Вывод на экран

print ("I'm going to write these to the file.")

# Вызов переменной target и запись в нее значения переменной line1

target.write(line1)

# -\\- и запись в нее ключа о переходе на новую строку

target.write('\n')

# -\\- и запись в нее значения значения переменной line2

target.write(line2)

# -\\- и запись в нее ключа о переходе на новую строку

target.write('\n')

# -\\- и запись в нее значения значения переменной line3

target.write(line3)

# -\\- и запись в нее ключа о переходе к новой строке

target.write('\n')

# Вывод на экран

print ('And finally, we close it.')

# Закрывает файл по принципу save\close

target.close()