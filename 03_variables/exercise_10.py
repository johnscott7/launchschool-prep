# Exercise 10
# Assume that obj already has a value of 42 when the code below starts running. 
# Which of the subsequent statements reassign the variable?
# Which statements mutate the value of the object that obj references? 
# Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd' # Re-assigns the variable
obj.upper() # Neither. Strings are immutable.
obj = obj.lower() # Re-assigns the variable
print(len(obj)) # Neither
obj = list(obj) # Re-assigns the variable
obj.pop() # Re-assigns the variable
obj[2] = 'X' # Mutates the value of the object
obj.sort()  # Mutates the value of the object
set(obj) # Neither
obj = tuple(obj) # Re-assigns the variable