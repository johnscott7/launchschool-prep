# Exercise 9
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal?
# Yes. Running print(my_list == list) will confirm it and print True, because their value is the same.

# Are the lists assigned to my_list and another_list the same object?
# No. It creates a new list object because constructors are non-mutating operations.
# Running print(my_list is list) will print False.

# Are the nested lists at index 3 of my_list and another_list equal?
# Yes, for the same reason as the first question. They share the same values.

# Are the nested lists at index 3 of my_list and another_list the same object?
# Yes. another_list is a shallow copy of my_list which means a new outer list is created, but the elements inside are not copied, only the referenes are re-used.

