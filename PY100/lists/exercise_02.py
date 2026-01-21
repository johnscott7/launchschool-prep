# Exercise 02
# Write a function that returns the last element of a list provided as an argument. For example:
# Be sure to handle the case where the input list is empty.

def last(my_list):
    if len(my_list) != 0:
        return my_list[-1]
    else:
        return "This list is empty"

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))