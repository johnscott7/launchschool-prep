# Exercise 05
# What will the following code do and why?

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# 1
# I believe the function will execute in the order it is written, meaning it will pull the value of a from the global scope.
# INCORRECT ANSWER

# CORRECT ANSWER:
# UnboundLocalError: cannot access local variable 'a' where it is not assocaited with a value
# When my_function() is compiled, Python detects that 'a' is being assigned within the function and therefore treats it as a local variable.
# However, at runtime, since print(a) is before the assignment, Python returns an error.
