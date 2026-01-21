# Exercise 10
# Write a function that counts the number of occurrences of a substring in a string.

def count_substrings(str_text, sub_text):
    index = 0
    count = 0
    for index in range (0, len(str_text)-len(sub_text)+1):
        test_slice = str_text[index:(index + (len(sub_text)))]
        if sub_text == test_slice:
            count += 1
    return count

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0