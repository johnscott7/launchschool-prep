# Exercise 2
# Without running this code, what will it print? Why?
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)
# Don't worry about having an exact match for the output. The important part is to show something that accurately represents set2.

# set1 and set2 both point to the same object in Python's heap
# Therefore, set2 when printed will show the range that has been added
# Output will look like:
# {42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}