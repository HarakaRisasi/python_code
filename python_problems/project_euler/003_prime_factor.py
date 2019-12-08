# n = int(input())
n = 6008513
div = []

for i in range(2, n):
    if n % i == 0:
        div.append(i)

print(div)