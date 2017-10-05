
name = input("Hello, what's youre name? ")

print("Hello %s, welcome to this program. " % name)

filename = input("Please enter your file name ")

print("\nHere are the contents of your file: \n ")
print(open(filename).read())

open(filename).close()
print("File closed ..Bye-bye")