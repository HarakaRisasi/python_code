# A two-digit number is conceived. 
# Find the probability that the conceived number will be: 
# a) a randomly named two-digit number; 
# b) a randomly named two-digit number, whose digits are different.

import subprocess
subprocess.call("clear")

def two_digits(m, n):
    p = m / n
    return int(p * 1000) / 10

# A)
favorable_outcomes_a = 1
outcomes_a = 99 - 10 + 1 
# because the 10 first digits is  0, 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 digits

# B)
favorable_outcomes_b = 1 # one of nine  11, 22, 33, ..., 99
outcomes_b = 90 - 9 # 90 - 9 or (11, 22, 33, ..., 99)

print(f'a)\n{favorable_outcomes_a} / {outcomes_a} or {two_digits(favorable_outcomes_a, outcomes_a)} %')
#>> 
# a)
# 1 / 90 or 1.1 %
print(f'b)\n{favorable_outcomes_b} / {outcomes_b} or {two_digits(favorable_outcomes_b, outcomes_b)} %')
#>> 
# b)
# 1 / 81 or 1.2 %