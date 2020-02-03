#There are 100 cars
cars= 100
#4 seats in the cars
space_in_a_car= 4.0
#there are 30 drivers
drivers= 30
#there are 90 passengers
passengers= 90
#cars not used
cars_not_driven= cars - drivers
#cars that are being driven 
cars_driven= drivers
#the amount of people that can carpool
carpool_capacity= cars_driven * space_in_a_car
#average amount of people per car
average_passengers_per_car= passengers//cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
#There was an error because there is an underscore after "car" in "carpool"
#1. It doesnt matter how you have "4" as long as you have it, the way you can change that is by add another dashed line while dividing like so "//"
#2. it can be placed anywhere relative to the significant digits of the number
j=13
i=26
print(j*i)
