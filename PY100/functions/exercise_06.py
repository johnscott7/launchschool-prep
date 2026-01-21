# Exercise 06
# Write a function that compares the length of two strings.
# It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length.
# For example:

# compare_by_length('patience', 'perseverance')
# compare_by_length('strength', 'dignity')
# compare_by_length('humor', 'grace')

def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0