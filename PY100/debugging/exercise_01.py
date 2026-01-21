# Exercise 1
# You come across the following code. 
# What errors does it raise for the given examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0) # Will error since it will only accept one argument (a list) and it has multiple integers
find_first_nonzero_among(1) # Will error since it is not a list

# TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
# TypeError: 'int' object is not iterable
