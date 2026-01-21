# Exercise 09
# What will the following code do and why?

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# 7
# Passing a parameter b to my_function() counts as intializing the variable, so there is no error
# When my_function(a) is called, Python creates a new local scope, evaluates the argument expression a -> object 7,
# then binds the parameter name b to that object, and then runs b += 10, resulting in variable 'b' pointing to the int object 17
# However, none of this changes the fact the global variable 'a' represents the value 7
