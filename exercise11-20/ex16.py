from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# "w" mode creates the file if it does not exist, and empties it if it does.
target = open(filename, 'w')

print("Trauncating the file. Goodbye!")
# There is no need for calling truncate function when we open the file with "w" mode
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(str(f"{line1}\n{line2}\n{line3}\n"))

print("And finally, we close it.")
target.close()