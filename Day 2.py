print("Day 2 - 100 Days of Code - Vani")
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $")) # string to float
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15? ")) # string to int
num_of_people = int(input("How many people to split the bill? ")) # string to int
total_tip = (tip_percentage/100)*total_bill # answer would be a floating point number
cost_per_person = (total_bill + total_tip)/num_of_people # floating point number
rounded_cost_pp = round(cost_per_person, 2) # floating point number with 2 decimal places
final_cost_pp = "{:.2f}".format(rounded_cost_pp) # to dispay two decimal places even though it's a 0. eg: 8.00
print(f"Each person should pay: ${final_cost_pp}") # f-string
