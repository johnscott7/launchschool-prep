# Exercise 07
# Write Python code to replace all the : characters in the string below with +.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
split_info = info.split(':')
rejoin_info = '+'.join(split_info)
print(rejoin_info)


# Try this problem using the methods you've learned about in this chapter. 
# Once you have that working, use the Python documentation for the str type to find an alternative solution.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = info.replace(':', '+')
print(new_info)
