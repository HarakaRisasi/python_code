# Init direct tilt ratio using numbers
A = 0.1

A_vis = A # Remember the initial value of direct tilt ratio

# The print of the initial direct data 
print(f'Initial direct: {A} * X')

# Speed of machine learning
lr = 0.001

# Initiate epoch numbers
epochs = 3000

# Create of input data array X
arr_x = [1, 2, 3, 3.5, 4, 6, 7.5, 8.5, 9]

# Create of output data array Y
arr_y = [2.4, 4.5, 5.5, 6.4, 8.5, 11.7, 16.1, 16.5, 18.3]

for e in range(epochs):
    for i in range(len(arr_x)):
        # Get a point coordinate like a value of X
        x = arr_x[i]

        # Get a calculated y, point coordinate
        y = A * x

        # Get target Y, point coordinate
        target_Y = arr_y[i]

        # Error E - target value - neuron output
        E = target_Y - y

        #  We change the x coefficient, in accordance with the rule A and Delta A
        A += lr * (E / x)

# Output of data ready to direct
print(f'Ready straight: y = {A} * X')

import matplotlib.pyplot as plt

# Function to display input
def func_data(x_data):
    return [arr_y[i] for i in range(len(arr_y))]

# Function to display the initial line
def func_begin(x_begin):
    return [A_vis * i for i in x_begin]

# Function to display the finished line
def func(x):
    return [A * i for i in x]

# X Input values
x_data = arr_x

# Values ​​on the X initial line (range of values)
x_begin = [i for i in range(0, 11)]

# Values ​​on X of the finished line (range of values)
x = [i for i in range(0, 11)]
# x = np.arange(0, 11, 1)

# Values ​​for Y input
y_data = func_data(x_data)

# Values ​​on Y starting line
y_begin = func_begin(x_begin)

# Y values ​​of the finished line
y = func(x)

# Define the names for the graph and numerical coordinates
plt.title("Neuron")
plt.xlabel("X")
plt.ylabel("Y")

# represent the data points (x, y) with circles of diameter 10
plt.scatter(x_data, y_data, color = 'g', s = 10)

# Start line
plt.plot(x_begin, y_begin, 'b')

# Finished direct
plt.plot(x, y, 'r')

# Grid in the background to improve perception
plt.grid(True, linestyle = '-', color = '0.75')

# Show graph
plt.show()

x = input('Input of width value X: ')
x = int(x)
T = input('Input of height value Y:')
T = int(T)
y = A * x

# Condition
if T > y:
    print('It\'s giraffe!')
else: 
    print('It\'s crocodile!')
