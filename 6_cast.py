#int(x)
#float(x)
#str(x)
#chr(x)
#unichr(x)
#ord(x)
#hex(x)
#oct(x)

a = input( 'Enter the number: ')
b = input( 'Now Enter Another Number: ')

sum = a + b
print('\nData Type sum: ', sum, type(sum))

sum = int(a) + int(b)
print('Data Type add: ', sum, type(sum))

sum = float(sum)
print('Data Type sum: ', sum, type(sum))

sum = chr( int( sum ) )
print( 'Data Type sum: ', sum, type(sum))
