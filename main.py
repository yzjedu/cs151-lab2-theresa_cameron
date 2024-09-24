# Enter Code here
# Read the README - under files on left
# Delete these three lines before submitting

#enter variables for birth, death and immigration rates
birth_rate = int(input("please enter birth rate: "))
death_rate = int(input("please enter death rate: "))
immigration = int(input("please enter immigrations rate: "))

#enter variables for current population, and number of projected years
current_pop = int(input("please enter current population: "))
num_years = int(input("please enter number of projected years in future: "))
print("")

#calculations for populations change and future populations
pop_change =
future_pop =

#output for populations change and future population
print("\nthe future population is ",future_pop, "and the change in population is", pop_change)


#population increase or decrease, or no change in population
if current_pop >= future_pop:
    print("population increased")
elif current_pop <= future_pop:
    print("populations decreased")
else:
    print("population did not change")