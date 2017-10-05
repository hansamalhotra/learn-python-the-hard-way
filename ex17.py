from sys import argv
from os.path import exists   #importing the function exists that we use later to check if a file exists or not

script, from_file, to_file = argv     #argv

print("Copying from %s to %s " % (from_file, to_file))

in_file = open(from_file)      #saving file object of from file in in_file, a new variable
indata = in_file.read()         #reading from_file's data

print("The input file is %d bytes long " % len(indata))     #finding the length of this datat

print("Does the output file exist? %r" % exists(to_file))   #checking if the destination file exists
print("Ready, hit return to continue, Ctrl-C to abort ")
input("?")

#saving file object of to_file into out_file, a new variable and using it to write indata on it
out_file = open(to_file,'w')   #opening in 'write' mode
out_file.write(indata)         #writing the contents of from_file on it

print("Alright, all done. ")

#closing the files
out_file.close()
in_file.close()
