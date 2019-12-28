# What is the largest prime factor of the number 600851475143 ?

import subprocess
subprocess.call("clear")

def factors(num):
    '''returns a list of the factors of num'''
    factorList = []
    for i in range(1, num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList

def largest_prime_factor(n):
    i = 2
    while i < n:
        if n % i:
            i += 1
        else:
            n //= i # Floor-Divide and Assign(//=)
    return n

print(factors(42))
print(largest_prime_factor(44))