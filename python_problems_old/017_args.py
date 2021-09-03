#_*_coding: utf-8_*_
#def func_name(arguments) - аргументы, необязательный параметр
#   после этого аргументу можно будет передать значение,
#   ссылаясь на имя аргумента функция будет использовать
#   переданное ей значение.

def echo( user ) :
    print('User: ', user )
#После того, как я положил в функцию аргумент, то ссылаясь на имя
#   аргумента я могу вызвать функцию и передать ей значение,
#   затем функция обработает полученное значение и выдаст результат.

#Теперь в вызове этой ф-и нужно указать значение, которое передается
#   аргументу в скобках для того, чтобы вывести его на печать
echo( 'Mike' )

def echo( user, lang, sys ) :
    print( 'User: ', user, 'Language: ', lang, 'System: ', sys )

echo( user = 'Alex', lang = 'Python', sys = 'Linux' )
#или
#echo( 'Alex', 'Python', 'Linux' )

#Указать заранее значение аргументов при определении ф-и

#!!! При помещения в ф-ю аргументов, будет ошибкой порядок
#    разположения их, если аргумент с ключевым словом будет стоять
#    перед простым аргументом.
# def func_name(arg_1, arg_2 = 'Hello', arg_3)

def echo( user, lang, sys = 'Linux' ) :
    print( 'User: ', user, 'Language: ', lang, 'System: ', sys )

echo(user = 'Alex', lang = 'Python' )

#Home work

def sum( a, b ) :
    return a + b
    
print ( "Sum of numbers is :", sum( 8, 4 ) )

# или

total = sum( 31, 234 )
print ( 'Sum of numbers is :', total )

