# _*_ coding: utf-8 _*_
#Чтобы интерпретатор узнал о наличии Юникода при выполнении программы#нужно добавить в программу специальный комментарий в ее начале.


#if   - проверка условия если то - то... 
# elif - проверка альтернативного условия если другое то - то...
# else - проверка условий не дала результат тогда то...

num = int(input('please enter a number: '))
if num > 5:
    print('Number exceeds five')
elif num < 5:
    print('Number is less than five')
else:
    print('Number is five')

if num > 7 and num < 9 :
    print('Number is 8')
if num == 1 or num == 3 :
    print('Number is 1 or 3')
