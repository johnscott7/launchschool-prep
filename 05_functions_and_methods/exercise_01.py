# Exercise 1
# What happens with the following program, and why?
def set_foo():
    foo = 'bar'
set_foo()
print(foo)

# This function assignments the variable foo the value 'bar'. 
# print(foo) will output an error because once the program steps out of the local function, the local variable does not exist in the global scope.