# Importing argv function from sys library in python
# Saving the cli arguments to variables
from sys import argv 
script, input_file = argv

# Function to read file & print it
def print_all(f):
	print(f.read())

# Function to get the cursor to the beginning of the file, coz after read() the cursor end-up in the bottom
def rewind(f):
	f.seek(0)

# Function to print the current line of the cursor & the content of that line.
def print_a_line(line_count, f):
	print(line_count, f.readline())

# File is opened & saving to a variable
current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 # current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # current_line = 2
print_a_line(current_line, current_file)

current_line += 1 # current_line = 3
print_a_line(current_line, current_file)