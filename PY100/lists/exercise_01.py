# Exercise 1
# Write a function that returns the first element of a list provided as an argument. For example:
# Be sure to handle the case where the input list is empty.

def first(my_list):
    if len(my_list) != 0:
        return my_list[0]
    else:
        return "This list is empty"

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))