formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",  #double quotes in output - bc there is already single quotes in didn't
    "So I said goodnight"
))