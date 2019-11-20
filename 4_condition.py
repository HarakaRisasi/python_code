#Ternary operator
#(test expression)  ?   if TRUE return this :   if FALSE return this
#if TRUE return this if (test expression)   else if FASLE return this
#c =   a   if (a   <   b)  else b
a   =   31
b   =   4
c   =   a   if  (a  >   b)  else    b
print c

d   =   a   if  (   a   %   2   !=  0)  else    b
print d

print(  '\nVariable a Is: ', 'Three' if (a  ==  1) else 'Not one')
print(  'Variable a Is: ', 'Even'  if( a  %   2   ==  0)  else 'Odd')

print(  '\nVariable b Is: ', 'One' if   (b  ==  1) else 'Not one')
print(  'Variable a Is: ', 'Even' if    (b % 2 == 0) else 'Odd')

max = a if  (a  >   b)  else b
print('\nGreater value is: ', max)
