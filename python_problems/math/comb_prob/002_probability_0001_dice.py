# dice
# need the probability of an even amount with at least one six
# P(A) = m / n

import subprocess
subprocess.call("clear")

def dice(m, n):
    p = m / n # in percent
    return int(p * 1000) / 10

favorable_outcomes = len([(6,2),(6,4),(6,6),(2,6),(2,4)])
outcomes = 6 * 6

print(f'Probability equal \n {favorable_outcomes} / {outcomes} \n or')
print(f' {dice(favorable_outcomes, outcomes)} %') 
#>> 
# Probability equal 
#  5 / 36 
#  or
#  13.8 %