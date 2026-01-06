# Exercise 3
# Without running this code, what will it print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# This creates a shallow copy
# Since a shallow copy does NOT inherent the same object, changing dict1 will not change dict2
# print will output 'The Life of Brian'