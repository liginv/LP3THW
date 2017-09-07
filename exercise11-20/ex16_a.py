from sys import argv

script, filename = argv
print(f"The file we about read is: {filename}\n")
file = open(filename)
print (file.read())