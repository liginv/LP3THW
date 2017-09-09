# This is a function which takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!") 
	print(f"YOu have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

# Calling the function directly by passing the values
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Creating varibales to store values
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Passing the variable names as arguments to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Doing arithmatic operation in the arguments of the function
print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Combining variables & arithmatic into function arguments
print("Add we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)