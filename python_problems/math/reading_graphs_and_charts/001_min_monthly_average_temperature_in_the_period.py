# Min monthly average temperature in the period

# Elements of the array, this is the average monthly temperature 
# in degrees in Sochi for each month of 1920. Determine the 
# lowest monthly average temperature from May to December 1920. 
# Give the answer in degrees Celsius.

year_celsius = [6, 4, 10, 14, 17, 21, 23, 24, 19, 13, 6, 7]
def min_middle_month_temp(arr):
    return min(arr[4:]) # get access the elements from index 'n' to the end

print('Min temperature from May to Dec is',min_middle_month_temp(year_celsius),'degrees')

#>> Min temperature from May to Dec is 6 degrees