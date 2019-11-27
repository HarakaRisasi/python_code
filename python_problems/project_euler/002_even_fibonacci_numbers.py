# Even Fibonacci numbers
#  Fn = Fn-1 + Fn-2 with seed values F0 = 0 and F1 = 1.

import subprocess # Calling an external command from Python
subprocess.run('clear')

def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  

nterms = int(input("Enter the terms? "))  # take input from the user
  
if nterms <= 0:  # check if the number is valid 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range((nterms)):
       print(FibRecursion(i), end=' ')