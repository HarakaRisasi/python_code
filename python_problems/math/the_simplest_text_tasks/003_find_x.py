# find x from equation '2 * x + 5 = 13'
# brute-force program that plugs in numbers to see which one satisfies the equation
def plug():
    # Я сделаю обоснованное предположение, что x - это значение между −100 и 100
    # так как 13 это двухзначное число. 
    # Поэтому поиск будет вестись в диапозоне чисел от -100 до 100
    x = -100 # start at -100
    while x < 100: # go to up to 100
        if 2 * x + 5 == 13:
            print('x =', x) # print it out
            break
        x += 1 # make x go up by 1 to test the next number

# run the plug function
plug() #>> x = 4