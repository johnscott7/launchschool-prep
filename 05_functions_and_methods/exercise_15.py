# Exercise 15
# Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.
def multiply(left, right):                                  # multiply (global), left (local), right (local)
    return left * right                                     # left (local), right (local)

def get_num(prompt):                                        # get_num (global), prompt (local)     
    return float(input(prompt))                             # float (built-in), input (local), prompt (local)

first_number = get_num('Enter the first number: ')          # first_number (global), get_num (global)
second_number = get_num('Enter the second number: ')        # second_number (global), get_num (global)
product = multiply(first_number, second_number)             # product (global), multiply (global), first_number (global), second_number (global)
print(f'{first_number} * {second_number} = {product}')      # print (built-in), first_number (global), second_number (global), product (local)


