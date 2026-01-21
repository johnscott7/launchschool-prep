# Exercise 03
# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return int(n) * 5 # Needed to add int() here around n, it was previously giving 1010101010 since it was taking the user input as a string.

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")