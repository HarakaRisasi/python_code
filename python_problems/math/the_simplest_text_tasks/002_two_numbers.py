# What greatest two numbers need to be multiplied to get 'n'
import subprocess
subprocess.call("clear")

n = 13195
div = []

# find all divisors
for i in range(2, n):
    if n % i == 0:
        div.append(i)

# search two largest divisors 
i = 0
while i < len(div)-1:
    x = (div[i] * div[i+1])
    if x == n:
        break
    i += 1

print(f'The two numbers are {div[i]} and {div[i+1]}')
