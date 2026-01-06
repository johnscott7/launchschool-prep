# Exercise 1
# The following code causes an infinite loop (a loop that never stops iterating). Why?
counter = 0

while counter < 5:
    print(counter)

# There is no change to the value of counter at any point. It will always stay 0, and therefore always be < 5, creating an infinite loop.