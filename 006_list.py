import subprocess
subprocess.call("clear")

x_set = [1, 1, 2, 3, 2, 6, 8, 3, 4, 5]
y, z = [], []

x_set = set(x_set)

for x_set in x_set:
    if (x_set % 2 == 0):
        y.append(x_set)
    else:
        z.append(x_set)
        
print(f'even {y} and odd {z}') #>> even [2, 4, 6, 8] and odd [1, 3, 5]