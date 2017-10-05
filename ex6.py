x = "There are %d types of people" % 10
binary = "binary"   #string with name binary takes "binary" in it
do_not = "don't"    #similar
#puts two strings inside a string
y = "Those who know %s and those who %s" % (binary,do_not)
#places with %s and %s get replaced by the string values of binary and do_not
print(x)
print(y)
#put string inside string
print("I said: %r" % x)    #%r displays the string exactly as it is with the quotes
#put string inside string
print("I also said: '%s'" % y)

hilarious = False
joke_evaluation="Isn't that joke so funny? %r"

print(joke_evaluation % hilarious)

w="This is the left side of..."
e="a string with a right side."
print(w+e)  #string concatenation