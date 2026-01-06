# Exercise 5
# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# [] are considered falsy, therefore my_list is considered False, so it will print 'Empty'