dict = {'name' : 'Alex', 'ref' : 'Python', 'sys' : 'Lin'}
print('Dictionary', dict)

print('\nReference: ', dict['ref'])

print('\nKeys: ', dict.keys())

del dict['name']

dict['user'] = 'Tom'
print('\nDictionary: ', dict)

dict['name'] = 'Alex'
print('\nIs there a name key?: ', 'name' in dict)
