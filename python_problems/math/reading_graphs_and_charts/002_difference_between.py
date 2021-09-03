# Determine from the figure the difference between 
# the largest and smallest audience in the specified period.

def diffAuditory(arr):
    return (max(arr) - min(arr)) * 10000

print(diffAuditory([325, 315, 320, 340, 318, 280, 290, 310, 305, 315, 345]))

#>> difference between max and min = 650000