# Exercise 8
# What does the following code do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# I suspect it will error since the function has two parameters but has three arguments passed to it.
# It is possible it will run using only the first two arguments, but my guess is an error.