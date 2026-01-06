# Exercise 15
# Without running the following code, what values will be printed by line 10?
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()          # this is a dictionary view object, which is a live view of the dictionary keys
del pets['Dog']             # pets = {'Cat': 'Meow', 'Bird': 'Tweet'}
pets['Snake'] = 'Sssss'     # pets = {'Cat': 'Meow', 'Bird': 'Tweet', 'Snake': 'Sssss'}
print(keys)                 # dict_keys(['Cat', 'Bird', 'Snake'])

