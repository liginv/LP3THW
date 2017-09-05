# Assigning variables to an interger & strings
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
don_not = "don't"
y = f"Those who know {binary} and those who {don_not}."
# Print the variables x & y
print(x)
print(y)
# Print x & y in a formatted way
print(f"I said: {x}")
print(f"I also said: '{y}'")
# Assigning variable to boolean & string
hilarious = False
joke_evaluvation = "Isn't that joke so funny?! {}"
# Print variable within a variable
print(joke_evaluvation.format(hilarious))
# Assigning two variables to string
w = "This is the left side of..."
e = "a string with a right side."
# Concatinating two strings
print(w + e)