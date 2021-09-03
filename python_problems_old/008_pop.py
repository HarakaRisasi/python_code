basket = ['Apple', 'Bun','Cola']
crate = ['Egg','Fig','Grape']
print('Basket List:', len(basket))

basket. append('Damson')
print('Appended:', basket)
print('Last Item Removed: ', basket.pop())
print('Basket List: ', basket)

basket.extend(crate)
print( 'Extended: ', basket)
del basket[1]
print('Item Reoved: ', basket)
del basket[1:3]
print('Slice Removed: ', basket)
