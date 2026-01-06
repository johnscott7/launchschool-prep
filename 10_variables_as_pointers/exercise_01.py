# Exercise 1
# In your own words, explain the difference between these two expressions.
my_object1 == my_object2
my_object1 is my_object2

# == represents equality, so for example 42 == 42
# is represents the two values being the same object in python's memory
# A good example to contrast the two would be two lists that look the same.
# You might have two lists that are  both [1, 2, 3], but they are unique objects. In this case,
# [1, 2, 3] == [1, 2, 3] will return True, but
# [1, 2, 3] is [1, 2, 3] would return False