


numbers = []

#converting it into a function
def make_a_list(last):
    i = 0
    while i < last:
        numbers.append(i)
        i += 1

last = input("Enter the last number ")
num = int(last) + 1
make_a_list(num)

print("Number is ", numbers)
