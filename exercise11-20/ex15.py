# Importing the function/module argv from sys library in python
from sys import argv
# Assigning the varable script & filename to argv function
script, filename = argv
# Saving the open function result to a variable txt.
# Open function is the file .txt file.
txt = open(filename)
# Printing the file name.
print(f"Here's your file {filename}:")
# Printing the content of the file.
print(txt.read())
# Closing the file.
txt.close()

# trying with inout alone.
file = input("Enter the file name: ")
txt1 = open(file)
print(txt1.read())
txt1.close()