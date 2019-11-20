#_*_coding: utf-8_*_
#lambda - в отличии от (def), данная ф-я не именуется и считается
#         анонимной.
#!!!Может содержать только одно выражение, которое должно всегда
#   возвращать значение.

#при def 
def square( a ) :
    return a ** 2, b ** 3


num = raw_input( 'input digit : ' )

a = b = int(num)
print(a, 'square and cube is equals: ', square(a) )
