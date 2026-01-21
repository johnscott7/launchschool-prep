# Exercise 07
# What will the following code do and why?

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# 2
# The value for print(a) will come from the global scope, however,
# the global scope value is re-written from within my_function() with the addition of 'global a' above 'a = 2'

