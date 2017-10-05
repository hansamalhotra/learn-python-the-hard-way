#Now changing while loop to for loop
#Do not need the i += increment part anymore 

numbers = []


def make_a_list(last, increment):
    for i in range(0,last, increment):
        numbers.append(i)


last = int(input("Enter the last number ")) + 1

inc = int(input("Enter the increment "))
make_a_list(last, inc)

print("Number is ", numbers)
