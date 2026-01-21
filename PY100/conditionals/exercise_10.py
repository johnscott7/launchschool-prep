# Exercise 10
# Determine what the following code snippet prints. 
# First solve it in your head or on paper, then run it in your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# This will print True
# Technically we do not need the parentheses because the accelration > 0 condition is True