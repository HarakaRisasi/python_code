# Словари связывают ключ со значением в других языках они могут называться 
# хешами, хеш-картами, картами или ассоциативными массивами

info = {
    1: 'Pete', 
    2: 'Best'
    }
print(info) #>> {1: 'Pete', 2: 'Best'}

# The paste value in the dict.
info[3] = 30
print(info) #>> {1: 'Pete', 2: 'Best', 3: 30}

# The check key
print(2 in info) #>> True
print(4 in info) #>> False

# dict. search
data = {'Alpha': 2, 'Gamma': 5, 'Beta': 1}
for name in data:
    print(name)
    #>>
    # Alpha
    # Gamma
    # Beta

# dict. search (value only)
for value in data.values():
    print(value)
    # 2
    # 5
    # 1

# dict. search (key, value)
for key, value in data.items():
    print(key, value)
    # Alpha 2
    # Gamma 5
    # Beta 1

# list
print(list(data.items())) #>> [('Alpha', 2), ('Gamma', 5), ('Beta', 1)]

# Помните, что словарь упорядочивается в порядке вставки ключей. Если
# вам нужен другой порядок, последовательность перебора необходимо отсортировать.
for name in sorted(data.keys()):
    print(name)
    #>>
    # Alpha
    # Beta
    # Gamma