# Even Fibonacci numbers
#  Fn = Fn-1 + Fn-2 with seed values F0 = 0 and F1 = 1.

a, b = 1, 1
total = 0

while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b  # the real formula for Fibonacci sequence
    
print (total) #>> 4613732