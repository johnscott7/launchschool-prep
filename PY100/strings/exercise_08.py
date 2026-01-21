# Exercise 08
# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.
import string
words = 'launch school tech & talk'
upper_words = string.capwords(words)
print(upper_words)