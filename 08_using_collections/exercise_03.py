# Exercise 03
# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)
rev_list = list(reversed(my_tuple))
rev_list = rev_list[1:-1]
rev_tuple = tuple(rev_list)
print(rev_tuple)
