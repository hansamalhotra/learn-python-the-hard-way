input_file = input("Enter the file name: ")

def print_all(f):
    print(f.read())

def rewind(f):
    # seek goes to the beginning of the file
    f.seek(0)

#displays the file count and reads a line from the file
def print_a_line(line_count,f):
    print(line_count)
    print(f.readline())

current_file = open(input_file)

print("First, let's print the whole file: \n")

print_all(current_file)

#This rewinding part is important, because file is currently at the end and it won't read
print("Now let's rewind, kind of like a tape..")
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

