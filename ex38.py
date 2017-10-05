
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there aren't 10 things in that list, let's fix that")

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items in the list now" % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print("My stuff now: ", stuff)  #corn has been removed from the list due to stuff.pop() in the previous line

#joining the different elements of list 'stuff' with a blank space ' '
print(' '.join(stuff))

#joining the elements from index value 3 to 5 with a #
print('#'.join(stuff[3:5]))

