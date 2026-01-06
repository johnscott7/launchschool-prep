# Exercise 2
# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
stuff = ('hello', 'world', 'bye', 'now')

# Tuples are immutable, so no. But, you can create a copy.
new_stuff = list(stuff)
new_stuff[2] = 'goodbye'
print(new_stuff)