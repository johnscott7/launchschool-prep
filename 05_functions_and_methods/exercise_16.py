# Exercise 16
# Identify all of the function names and parameters present in the code. Include the line numbers for each item identified.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply is a function name (line 3, line 11)
# get_num is a function name (line 6, 9, and 10)
# left and right are parameters (lines 3 and 4)
# prompt is a parameter (line 6 and line 7)
# float (5), input(5) and print(10) are also built-in functions
