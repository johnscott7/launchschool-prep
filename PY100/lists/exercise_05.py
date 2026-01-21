# Exercise 05
# Count the number of elements in scores that are 100 or above.
scores = [96, 47, 113, 89, 100, 102]
count = 0
for element in scores:
    if element >= 100:
        count += 1
print(count)