# 1. Declare and assign the variables here:
shuttle = "Determination"
speed_mph = 17500
mars_dist_km = 225000000
moon_dist_km = 384400
miles_pr_km = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle))
print(type(speed_mph))
print(type(mars_dist_km))
print(type(moon_dist_km))
print(type(miles_pr_km))
# Code your solution to exercises 3 and 4 here:
miles_to_mars = mars_dist_km * miles_pr_km
hours_to_mars = miles_to_mars / speed_mph
days_to_mars = hours_to_mars / 24 
# Code your solution to exercise 5 here
print(shuttle + " will take " + str(days_to_mars) + " days to reach the Moon.")