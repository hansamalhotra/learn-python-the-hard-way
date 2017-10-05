#importing ex25 into python as a module which makes all the functions usable
import ex25

#Makes a sentence to work with
sentence = "All good things come to those who wait"

#call a function from the ex25 module
words = ex25.break_words(sentence)

#printing the above
print(words)

#Sorting the words
sorted_words = ex25.sort_words(words)
print(sorted_words)

#Printing the first and last words
ex25.print_first_word(words)
ex25.print_last_word(words)

print(words)

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)

print(sorted_words)

sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)

#asking for help
help(ex25)