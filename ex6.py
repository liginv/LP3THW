types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
don_not = "don't"
y = f"Those who know {binary} and those who {don_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluvation = "Isn't that joke so funny?! {}"

print(joke_evaluvation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)