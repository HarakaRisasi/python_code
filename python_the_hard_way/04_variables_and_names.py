#_*_coding:utf-8_*_
#init var and apropriate value for her
cars = 100
#init var and apropriate value for her
space_in_a_car = 4.0
#init var and apropriate value for her
drivers = 30
#init var and apropriate value for her
passengers = 90
#init var, after do cars minus drivers and aprop. this value for her
cars_not_driven = cars - drivers
#init var, after aprop. value of drivers
cars_driven = drivers
#init var, after aprop. her value by multiply two var
carpool_capacity = cars_driven * space_in_a_car
#init var, after aprop. her value by devision two var
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "each car."
