import subprocess
subprocess.call("clear")

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f'The {year} it\'s a leap year')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f'The {year} it\'s a leap year')
        else:
            print(f'The {year} was not a leap')
    else:
        print(f'The {year} was not a leap')

leap_year(1800) # False
leap_year(1900) # False
leap_year(1903) # False
leap_year(2000) # True
leap_year(2020) # True