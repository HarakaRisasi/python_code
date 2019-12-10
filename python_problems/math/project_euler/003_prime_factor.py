# What is the largest prime factor of the number 600851475143 ?

import subprocess
subprocess.call("clear")

def prime_factors(n):
    i = 2
    factors = []
    while i < n:
        if n % i:
            i += 1
        else:
            n //= i # Floor-Divide and Assign(//=)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def largest_prime_factor(n):
    i = 2
    while i < n:
        if n % i:
            i += 1
        else:
            n //= i # Floor-Divide and Assign(//=)
    return n


print(prime_factors(600851475143))
print(largest_prime_factor(600851475143))

print(prime_factors(13195))
print(largest_prime_factor(13195))