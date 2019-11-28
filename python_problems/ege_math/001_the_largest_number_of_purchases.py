# The largest number of purchases

# Notebook costs 40 rubles. What is the largest number of such notebooks 
# that can be bought for 750 rubles after lowering the price by 10%?

def largest_num(sum_rub):
    price_rub = 40 # price for one goods
    sale = 0.90 # 10% sale
    goods_amount = int(sum_rub // (price_rub * sale))
    return goods_amount

print(largest_num(750),'such can be bought for 750 rubles')

#>> 20 notebooks can be bought for 750 rubles