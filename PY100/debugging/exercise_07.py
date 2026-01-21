# Exercise 07
# You are trying to access a value in a dictionary, but the code is giving you an error. 
# Can you change the print(info['city']) line so that it prints "Unknown" instead of raising an error?

info = {'name': 'Srdjan', 'age': 38}
print(info.get('city', 'Unknown'))