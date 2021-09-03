#_*_ coding: utf-8 _*_
#Continue - располагается внутри блока инструкций цикла
#           служит для пропуска одной из итераций(одно полное 
#           исполнение инструкции внутри цикла)
#range()  - функция генерирующая последовательность
#           range(4) = 0,1,2,3.

for i in range( 1, 4 ) :
    for j in range( 1, 4 ) :
        if i == 2 and j == 1 :
            print( 'Continues inner loop at i = 1 j = 1' )
            continue
        print('Running i =', i, 'j = ', j)
