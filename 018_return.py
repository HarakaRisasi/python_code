#_*_coding: utf-8_*_
#return - возвращает указанное значени оператору вызвавшему
#         инструкцию return

#в данном случае, если первый аргумент меньше пяти, то функция
#вернет (None), а последняя инструкция не станет исполняться.

def sum( a, b ) :
    if a < 5:
       return
    return a + b

print( 'Sum of two numbers is:', sum( 2, 43 ) )
print( 'Sum of two numbers is:', sum( 6, 3 ) )

#home work

#Raw_input () обрабатывает все входные данные как строку и возвращает#             тип строки.
#num = raw_input()

num = raw_input( 'Enter an integer: ' )

#.isdigit - метод проверяет переданное значение аргументу, является 
#           ли оно числом.
#           isgit() is a method of a str class. 

def square(num) :
    if num.isdigit() :
        num = int(num)
        return num * num
    return( 'input number is not digit' )

print( num, 'Squared is: ', square( num ) )
