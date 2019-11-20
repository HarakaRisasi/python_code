#   _*_coding:utf-8_*_
#   script - другое название программы с раcширением .py
#   argv(argument variable) - список аргументов(параметров) 
#   командной строки, передаваемых сценарию python (name_of_prog.py)
#   др.сл. программе python

from sys import argv

#   sys - это модуль(др. название - библиотека), содержит переменные
#   и функции, имеющие отношение к интерпретатору и его окружению.

script, first, second, third = argv

fourth = "enter your value: {0} ". format(input())

print ("The script is called:", script)       #argv[0]
#   The argv[0] - is the name of script

print ("Your first variable is:", first)      #argv[1]
print ("Your second variable is:", second)    #argv[2]
print ("Your third variable is:", third)      #argv[3]
print ("Your fourth variable is: ", fourth)   #out.val.of inp.function

#   !!!ADD name after ran the .py file
#   command line:
#   python 13_parameters_... . py aleksandr
#   or
#   python 13_parameters_... .py 1st 2nd 3rd
