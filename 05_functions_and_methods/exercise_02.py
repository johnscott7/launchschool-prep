# Exercise 2
# What does this program print? Why?
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# This program will print bar because, like example 1, set_foo only defines the variable foo within the local scope,
# and the print(foo) request is located within the global scope, where foo is defined as 'bar'.