# Exercise 06
# Write a function that checks whether a string is empty or not. For example:
def is_empty(x):
    if len(x) != 0:
        return False
    else:
        return True


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
