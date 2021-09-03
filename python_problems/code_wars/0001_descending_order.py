# Sort numbers in descending order
def Descending_Order(num):    
    return int(''.join(sorted(str(num))[::-1]))

print(Descending_Order(1021)) #=> 2110

#Discription:
#----------------------------------
# steps:
# 0 input num >> 1021
# 1 str(num) >> '1021' 
# 2 sorted(str(num)) >> ['0', '1', '1', '2']
# 3 [::-1] or reverse(slice list) >> ['2', '1', '1', '0']
# 4 join list to string >> '2110'
# 5 convert to int >> 2110
#----------------------------------   
#1
# Another solution
# return int(''.join(sorted(str(num), reverse=1)))

#2
# def Descending_Order(num):
# lst = (sorted(list(map(int, str(num))))[::-1])
# return int("".join(map(str, lst)))
#----------------------------------
# type check:
# type(str(num)) >> <class 'str'>
    
# type(int(str(num))) >> <class 'int'>
#----------------------------------