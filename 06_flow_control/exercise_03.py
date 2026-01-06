# Exercise 3
# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# The first output will be 'Product2', the second output will print 'Product not found!' since the first is a case match but the second is not since it is an integer, not a string.