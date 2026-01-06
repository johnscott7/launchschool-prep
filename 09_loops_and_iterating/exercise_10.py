# Exercise 10
# The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. 
# Using a while loop, it keeps running until it finds a random number that matches the last number in the range. 
# Refactor the code so it doesn't require two different invocations of randrange.

import random

# highest = 10
# number = random.randrange(highest + 1) # Select a random number in the range 0-11 and assign it to the variable number
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)  
#    print(number)

# Use python's version of a do/while loop

highest = 10
while True:
    number = random.randrange(highest + 1)  
    print(number)
    if number == highest:
        break