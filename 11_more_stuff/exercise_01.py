# Exercise 1
# What does the following function do? Be sure to identify the output value.
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# This function creates a sorted dictionary, and returns the second (1st-indexed) key in that dictionary, in all uppercase letters. In this case,
# CHRIS