# Exercise 07
# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:
def is_empty_or_blank(x):
    x = x.strip()
    return len(x) == 0


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
