# Programmers: Theresa DeJacimo and Cameron Combariza
# Course: CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: figure out population change, future population, and weather it increased/decreased
# Data In: seconds per year, birth rate, death rate, immigration rate, number of years in future
# Data Out: population change, future population, weather it increased or decreased
# Credits: [in class]



#enter variables for birth, death and immigration rates
seconds_per_year = 31536000
birth_rate = int(input("please enter birth rate: "))
death_rate = int(input("please enter death rate: "))
immigration = int(input("please enter immigrations rate: "))

#enter variables for current population, and number of projected years
current_pop = int(input("please enter current population: "))
num_years = int(input("please enter number of projected years in future: "))
print("")

#calculations for populations change and future populations
pop_change = (seconds_per_year/birth_rate + seconds_per_year/immigration - seconds_per_year/death_rate) * num_years
future_pop = pop_change + current_pop

#output for populations change and future population
print("\nthe future population is ",future_pop, "and the change in population is", pop_change)


#population increase or decrease, or no change in population
if current_pop < future_pop:
    print("population increased")
elif current_pop > future_pop:
    print("populations decreased")
else:
    print("population did not change")