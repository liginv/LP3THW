# Create a variable that have 4 placeholders
formatter = "{} {} {} {}"
# Printing the result with format method of print to the variable created above
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"or a song about fear"
))