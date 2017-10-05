from sys import argv    #imports the module argv which takes arguments from terminal

script, filename = argv    #assigns these arguments

txt = open(filename)   #opens the file you just passed through script and returns to object called txt

print("Here's your file %r: " % filename)   #display file name
print(txt.read())                           #reads your file

print("Type the file name again, por favor ")
file_again = input("> ")                   # asks for input of filename again

txt_again = open(file_again)               # similar

print(txt_again.read())                    #similar 


