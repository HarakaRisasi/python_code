#_*_ coding: utf-8 _*_

from __future__ import print_function

for i in range( 1, 4 ) :
    for j in range( 1, 4 ) :
        if i == 2 and j == 1 :
            print( 'Breaks inner loop at i = 2 j = 1' )
            break
        print('Running i =', i, 'j = ', j)
    
for i in 'hello world' :
    if i == 'o' :
        break
    print( i * 2, end = ' ')
print( '\n' )
