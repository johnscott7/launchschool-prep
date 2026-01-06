# Exercise 3
# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(num1, num2):
    return num1 * num2


x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
answer = multiply(x, y)
print(f'The result of multiplying {x} and {y} is {answer}.')
