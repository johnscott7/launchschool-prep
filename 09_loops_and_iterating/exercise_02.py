# Exercise 02
# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter.
# The updated code should use a for loop to display the future ages.

age = input('How old are you, my friend? ')
for years in range(10, 50, 10):
        print(f'In {years} years, you will be {int(age) + years} years old.')
        
