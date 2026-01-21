# Exercise 06
# You've been given a list of vocabulary words grouped into sub-lists, by meaning. 
# This is a two-dimensional list or a nested list. Write some code that iterates through and prints all the words, one per line.
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

def print_sublists(my_list):
    x = 0
    while x < len(my_list):
        y = 0
        while y < len(my_list[x]):
            print(my_list[x][y])
            y += 1
        x += 1

print_sublists(vocabulary)

# A cleaner approach uses a for loop since it loops over items in a list:
def print_vocabulary_words(vocabulary):
    for group in vocabulary:
        for word in group:
            print(word)

print_vocabulary_words(vocabulary)