cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Prints string "There are" than the variable cars(100) and than the string cars avaible"
print "There are", cars, "cars available."
# Prints String "There are only" than the vairbale drivers (30) and than the string "drivers availible"
print "There are only", drivers, "drivers available."
# Print the string "There will be" than the variable cars_not_driven ( 100 - 30 = 70)
print "There will be", cars_not_driven, "empty cars today."
# Prints the string "We can transport" than the variable carpool_capacity (30 * 4.0  = 120.0)
print "We can transport", carpool_capacity, "people today."
# Prints the string "We have" than the variable passengers (90) than thte string "to carpool today."
print "We have", passengers, "to carpool today."
# Prints out the string "We need to put about" than the variable average_passengers_per_car (90 / 30 = 3) than the string "in each car."
print "We need to put about", average_passengers_per_car, "in each car."
