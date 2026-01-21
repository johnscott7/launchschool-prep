# Exercise 10
# What will the following code do and why?

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# [10, 2, 3]
# [1, 2, 3] is a mutable list
# In the other examples we were re-assigning variables new values
# In this case, the function mutates the list object, so when my_function() is called, 
# the list object is mutated, and print(b) shows the current state of that object