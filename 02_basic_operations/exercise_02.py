# Exercise 2
# Use the REPL and arithmetic operators to extract the individual digits of 4936:
# 1. One place is a 6.
# 2. Tens place is a 3.
# 3. Hundreds place is a 9.
# 4. Thousands place is a 4.

number = 4936
ones_number number % 10
tens_number = (number // 10) % 10
hundo_number = (number // 100) % 10
thous_number = (number // 1000) % 10
print(ones_number, tens_number, hundo_number, thous_number)