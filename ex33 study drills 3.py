

numbers = []

#last and increment arguments for the last number of the list and the incremental value resp
def make_a_list(last, increment):
    i = 0
    while i < last:
        numbers.append(i)
        i += increment

last = int(input("Enter the last number ")) + 1

inc = int(input("Enter the increment "))
make_a_list(last, inc)

print("Number is ", numbers)
