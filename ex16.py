from sys import argv

script, filename = argv

print("We're going to erase %r" % filename)
print("If you don't want that, hit Ctrl-C ")
print("If you want that, hit Return Key")

input("? ")

print("Opening the file...")
target = open(filename, 'w')



print("\nTruncating the file. Goodbye! ")
target.truncate()

print("Now I'm going to ask you for three lines ")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file. ")

target.write("%s\n%s\n%s" % (line1, line2, line3))


print("And now we close the file")
target.close()