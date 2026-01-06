# Exercise 4
# Without running this code, what will it print? Why?
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# [1, 2, 3] is an object on its own, so the shallow copy created here, points to the same list object for ['a'][1]
# As a result, changing this list object via dict1 will also change what the variable is pointing to in dict2
# Output will be:
# [1, 42, 3]