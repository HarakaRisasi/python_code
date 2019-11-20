#initialization variable
a   =   True
b   =   False

#get instruction AND
print(  'AND Logic:')
print(  'a and b = ',   a and a)
print(  'a and b = ',   a and b)
print(  'a and b = ',   b and b)

#get instruction OR
print(  '\nOR Logic:'    )
print(  'a or a = ',    a or a)
print(  'a or b = ',    a or b)
print(  'b or b = ',    b or b)

#get instruction NOT
print(  '\nNOT Logic:'  )
print(  'a = ', a, 'not a = ', not a)
print(  'b = ', b, 'not b = ', not b)

#Ternary operator
#(test expression)  ?   if TRUE return this :   if FALSE return this
#if TRUE return this if (test expression)   else if FASLE return this
#c =   a   if (a   <   b)  else b
a   =   3
b   =   4
c   =   a   if  (a  >   b)  else    b
print c

d   =   a   if  (   a   %   2   !=  0)  else    b
print d
