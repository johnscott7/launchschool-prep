# Exercise 10
# Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for num in numbers:
    print(f'A {num} number is {numbers[num]}')


'''Expected Output:
A high number is 100.
A medium number is 50.
A low number is 10.
'''

